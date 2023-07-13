#!/usr/bin/python3
"""a Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a
parameter
"""
import sys
import requests


def main():
    email = {'email': sys.argv[2]}
    url = sys.argv[1]
    r = requests.post(url, data=email)
    print(r.text)

if __name__ == '__main__':
    main()
