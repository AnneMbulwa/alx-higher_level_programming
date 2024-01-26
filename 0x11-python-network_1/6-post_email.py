#!/usr/bin/python3
"""takes in a URL and an email address, sends a POST request to
the passed URL with the email as a parameter
using requests"""
import requests


if __name__ == "__main__":
    email = {'email': argv[2]}
    respone = requests.post(argv[1], data=email)
    print(reaponse.text)
