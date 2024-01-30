#!/usr/bin/python3
"""takes your GitHub credentials (username and password) and
uses the GitHub API to display your id"""

from urllib import requests
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]

    auth = (username, password)
    res = requests.get("https://api.github.com/user", auth=auth)
    print(res.json().get("id"))
