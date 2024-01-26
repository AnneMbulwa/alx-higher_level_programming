#!/usr/bin/python3
"""manage urllib.error.HTTPError exceptions"""
from urllib import error, request
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    try:
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as myerr:
        print("Error code: ", myerr.code)
