 #!/usr/bin/python3
 import urllib.request
 import urllib.parse
 import sys


 if __name__ == "__main__":
     values = {'email' : sys.argv[2]}
     data = urllib.parse.urlencode(values)
     data = data.encode('utf-8')
     req = urllib.request.Request(sys.argv[1], data)
     with urllib.request.urlopen(req) as response:
            the_page = response.read()
            print(the_page)
