#!/usr/bin/python3
"""dsdfdf f f dfdf"""
import requests
import sys
if __name__ == "__main__":
     r = requests.get(sys.argv[1])
     print(r.text)