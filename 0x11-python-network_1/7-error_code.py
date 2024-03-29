#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to
the URL and displays the body of the response
"""
import sys
import requests


def main():
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print('Error code: {}'.format(r.status_code))
    else:
        print(r.text)


if __name__ == '__main__':
    main()
