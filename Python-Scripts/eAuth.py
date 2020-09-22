#!/usr/bin/env python3

from eAsistent import getNewToken
from os import environ

with open("/home/r1c/stvari/koda.txt", "r") as koda:
      koda = koda.read()


auth = getNewToken(environ.get("EA_Uporabnik"), koda)         
with open("/home/r1c/stvari/auth.txt", "wb") as f:
      f.write(bytes("{}{}".format(auth[0], "\n"), "UTF-8"))
      f.write(auth[1])
