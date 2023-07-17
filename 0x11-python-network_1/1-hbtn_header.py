#!/usr/bin/python3
"""Write a Python script that takes in a URL, sends a
    request to the URL
    """
import urllib.request
import sys


def main():
    with urllib.request.urlopen(sys.argv[1]) as f:
        info = f.info()
        print(info['X-Request-Id'])


if __name__ == '__main__':
    main()
