#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    resv = requests.get("https://alx-intranet.hbtn.io/status")
    conv = resv.text
    print("Body response:")
    print("\t - type:", type(conv))
    print("\t - content:", conv)
