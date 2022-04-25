#!/usr/bin/python3
"""0. What's my status? #0"""
import requests
if __name__ == "__main__":
    html = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(html.text)))
    print("\t- content: {}".format(html.text))
