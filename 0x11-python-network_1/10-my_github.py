#!/usr/bin/python3
"""a Python script that takes your GTHub credentials and
uses the GitHub API to display id
"""
import sys
import requests


def main():
    url = "https://api.github.com/user"
    payload = (sys.argv[1], sys.argv[2])
    r = requests.get(url, auth=payload)
    print(r.json().get('id'))


if __name__ == '__main__':
    main()
