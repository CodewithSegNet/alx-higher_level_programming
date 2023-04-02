#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status """
import requests


url = 'https://alx-intranet.hbtn.io/status'

req = requests.get(url)

print("Body response:")
print("\t- type: {}".format(type(req.text)))
print("\t- content: {}".format(req.text))
