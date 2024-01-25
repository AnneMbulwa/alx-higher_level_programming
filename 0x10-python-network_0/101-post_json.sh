#!/bin/bash
# with using curl to send a JSON POST request to a URL passed as 1st argv
curl -s -X POST -d "@$2" -H "Content-Type: application/json" "$1"
