#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""

from urllib import request


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    with request.urlopen(url) as response:
        value = response.read()
        print("Body response:")
        print("\t - type: {}".format(type(value)))
        print("\t - content: {}".format(value))
        print("\t - utf8 content: {}".format(value.decode('utf-8')))
