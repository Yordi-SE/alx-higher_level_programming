#!/usr/bin/python3
"""Python script that takes in a letter and sends a
POST request to URL with the letteras a parameter
"""
import sys
import requests


def main():
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        q = {'q': sys.argv[1]}
    else:
        q = {'q': ""}
    r = requests.post(url, params=q)
    try:
        rr = r.json()
        print('[{}] {}'.format(rr.get('id'), rr.get('name')))
    except Exception:
        if r.status_code == 204:
            print('No result')
        else:
            print('Not a valid JSON')


if __name__ == '__main__':
    main()
