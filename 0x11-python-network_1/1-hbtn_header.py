#!/usr/bin/python3
"""1. Response header value #0"""
import urllib.request
import sys



if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        the_page = response.headers['X-Request-Id']
        print(the_page)
