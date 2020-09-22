#!/usr/bin/env python3

from bs4 import BeautifulSoup
import json
import requests


def getNewToken(uporabnik: str, geslo: str):
	"""
	Pridobi access-token in child-id, ki sta potrebna za ustvarjanje primerka razreda eAsistent in dostopanje do eAsistent API-ja
	"""

	loginData = {"uporabnik": uporabnik, "geslo": geslo}
	s = requests.Session()

	login = s.post("https://www.easistent.com/p/ajax_prijava", data = loginData)

	if json.loads(login.text)["status"] != "ok":
		return "Napačno uporabniško ime ali geslo! Poskusite znova!"

	else:
		src = s.get("https://www.easistent.com").text
		soup = BeautifulSoup(src, "html.parser")

		access_token = soup.find("meta", attrs = {"name": "access-token"})
		child_id = soup.find("meta", attrs = {"name": "x-child-id"})

		return access_token["content"], child_id["content"]


class eAsistentClient:
	"""
	Predstavlja uporabnika eAsistenta za katerega so na voljo razne metode za dostop do ocen, ocenjevanj znanja, urnika...
	"""
	def __init__(self, access_token, child_id):
		self.s = requests.Session()
		self.headers = {
			"accept": "application/json, text/javascript, */*; q=0.01",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": "sl,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,cy;q=0.6",
			"authorization": str(access_token),
			"referer": "https://www.easistent.com/webapp",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin",
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.44",
			"x-child-id": str(child_id),
			"x-client-platform": "web",
			"x-client-version": "13",
			"x-requested-with": "XMLHttpRequest"
		}


	def refreshAuthorization(self, new_token):
		"""
		Osveži JWT potreben za dostopanje do eAsistent API-ja (JWT poteče po 24 urah, zato je potrebno pridobiti novega z uporabo funkcije getNewToken())
		"""
		self.headers["authorization"] = str(new_token)
		return new_token


	def getPastEvaluations(self):
		"""
		Pridobi pretekla ocenjevanja znanja
		"""
		r = self.s.get("https://www.easistent.com/m/evaluations?filter=past", headers = self.headers)
		
		try:
			if json.loads(r.text)["error"]:
				return "Neveljaven access_token in/ali child_id"
		except:
			return json.loads(r.text)


	def getFutureEvaluations(self):
		"""
		Pridobi prihodnja ocenjevanja znanja
		"""
		r = self.s.get("https://www.easistent.com/m/evaluations?filter=future", headers = self.headers)
		
		try:
			if json.loads(r.text)["error"]:
				return "Neveljaven access_token in/ali child_id"
		except:
			return json.loads(r.text)


	def getSchedule(self):
		"""
		Pridobi urnik za trenutni dan
		"""
		r = self.s.get("https://www.easistent.com/m/timetable/weekly", headers = self.headers)

		try:
			if json.loads(r.text)["error"]:
				return "Neveljaven access_token in/ali child_id"
		except:
			return json.loads(r.text)


	def getGrades(self):
		"""
		Pridobi ocene
		"""
		r = self.s.get("https://www.easistent.com/m/grades", headers = self.headers)

		try:
			if json.loads(r.text)["error"]:
				return "Neveljaven access_token in/ali child_id"
		except:
			return json.loads(r.text)