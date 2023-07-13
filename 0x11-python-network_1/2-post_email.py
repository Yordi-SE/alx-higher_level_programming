#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST
request to the passed URl with the email as
"""
import sys
import urllib.request
import urllib.parse


def main():
    email = {'email':sys.argv[2]}
    email = urllib.parse.urlencode(email)
    email = email.encode('ascii')
    url = sys.argv[1]
    req = urllib.request.Request(url, email)
    with urllib.request.urlopen(req) as f:
        body = f.read()
        print(body.decode('utf-8'))


if __name__ == '__main__':
    main()
