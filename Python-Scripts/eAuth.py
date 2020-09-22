#!/usr/bin/env python3

from eAsistent import getNewToken
from os import environ
from time import sleep


def getToken():
    while True:
        auth = getNewToken(environ.get("EA_Uporabnik"), environ.get("EA_Geslo"))
            
        with open("auth.txt", "w") as f:
            f.write(f"{auth[0]}\n")
            f.write(auth[1])

        sleep(43200)

getToken()