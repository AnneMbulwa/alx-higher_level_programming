#!/bin/bash
# using curl send DELETE request to the url passed as the first argument and
# display the body of response

curl -s -X DELETE "$1"
