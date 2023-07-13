#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request


def main():

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as s:
        f = s.read()
        print('Body response:$')
        print('\t- type: {}$'.format(type(f)))
        print('\t- content: {}$'.format(f))
        print('\t- utf8 content: {}$'.format(f.decode('utf-8')))


if __name__ == '__main__':
    main()
