#!/usr/bin/python3
"""Python script that takes in a URL, sends a request ot the URL
and dispalyas the body of the response
"""
import urllib.request
import sys
import urllib.error


def main():
    try:
        with urllib.request.urlopen(sys.argv[1]) as f:
            body = f.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == '__main__':
    main()
