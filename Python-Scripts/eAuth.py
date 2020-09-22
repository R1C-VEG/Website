#!/usr/bin/env python3

from eAsistent import getNewToken
from os import environ

with open("koda.txt", "r") as koda:
      koda = str(koda.read()).replace("\n", "")


auth = getNewToken(str(environ["EA_Uporabnik"]), koda)         
with open("auth.txt", "wb") as f:
      f.write(bytes("{}{}".format(auth[0], "\n"), "UTF-8"))
      f.write(auth[1])
