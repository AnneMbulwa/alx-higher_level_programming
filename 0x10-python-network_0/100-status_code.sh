#!/bin/bash
# using curl to send request to URL passed as argument and display status code
curl -s -o /dev/null -w "%{http_code}" "$1"
