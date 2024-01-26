#!/usr/bin/python3
"""displaying the value of the X-Request-Id variable found in the
header of the response.
"""
from urllib import request
import sys


if __name__ == "__main__":

    url = sys.argv[1]

    with request.urlopen(url) as response:
        body = response.getheader('X-Request-Id')
        print(body)
