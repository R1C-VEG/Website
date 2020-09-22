#!/usr/bin/env python3

from eAsistent import eAsistentClient
import json


with open("Python-Scripts/auth.txt", "r") as f:
    auth = f.readlines()

eAC = eAsistentClient(auth[0][:-1], auth[1])

print(json.dumps(eAC.getFutureEvaluations(), indent = 4))