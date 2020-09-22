#!/usr/bin/env python3

from eAsistent import getNewToken
from os import environ

with open("koda.txt", "r") as koda:
      koda = koda.read()


auth = getNewToken(environ.get("EA_Uporabnik"), koda)         
with open("auth.txt", "w") as f:
      f.write("{}{}".format(auth[0], "\n"))
      f.write(auth[1])