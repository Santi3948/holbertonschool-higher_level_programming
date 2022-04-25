#!/usr/bin/python3
"""1. Response header value #0"""
import requests
import sys

if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    print(req.headers['X-Request-Id'])
