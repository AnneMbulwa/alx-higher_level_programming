#!/bin/bash
# with using curl to send a JSON POST request to a URL passed as the
# first argument, and displays the body of the response.
# must send POST request

curl -s -X POST -d "@2" -H "Content-Type: application/json" "$1"
