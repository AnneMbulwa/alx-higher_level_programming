#!/usr/bin/python3
"""manage urllib.error.HTTPError exceptions"""
import urllib.error
import urllib.request
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    try:
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as myerr:
        print("Error code: ", myerr.code)
