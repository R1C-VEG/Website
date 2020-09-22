#!/usr/bin/env python3

from eAsistent import getNewToken
from os import environ

auth = getNewToken(environ.get("EA_Uporabnik"), environ.get("EA_Geslo"))         
with open("auth.txt", "w") as f:
      f.write(f"{auth[0]}\n")
      f.write(auth[1])
