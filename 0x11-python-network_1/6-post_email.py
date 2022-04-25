#!/usr/bin/python3
"""6. POST an email #1"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    data = {'email': email}
    req = requests.post(url, data)
    print(req.text)
