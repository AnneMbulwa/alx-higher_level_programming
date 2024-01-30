#!/usr/bin/python3
"""display error code of http status code"""

from urllib import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    res = requests.get(url)
    cos = res.text
    print(cos)

    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
