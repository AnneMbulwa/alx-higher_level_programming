#!/usr/bin/python3
"""sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter."""
from urllib import requests
from sys import argv


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = argv[1] if len(argv) > ""
    letter = {"q": q}

    res = response.post(url, letter)
    try:
        json_res = response.json()
        if json_res:
            print("[{json_res("id"} {json_res("name"}]")
        else:
            print("No result")
    except ValueError:
        print("Not a valid json")
