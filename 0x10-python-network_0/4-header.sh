#!/bin/bash
# with using curl take in a URL as an argument, sends a GET request to the URL,
# and displays the body of the response
# header variable X-School-User-Id with the value 98 must be send

curl -sH "X-School-User-Id: 98" "$1"
