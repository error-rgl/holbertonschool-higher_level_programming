#!/usr/bin/python3
"""
Python script that fetches an URL with requests package
"""
import requests


if __name__ == "__main__":
    resp = requests.get('https://intranet.hbtn.io/status')
    cont = resp.text
    print("Body response:")
    print("\t- type: {}".format(type(cont)))
    print("\t- content: {}".format(cont))
