#!/bin/bash
# using curl, send a POST request to the passed URL with the variable email and
# subject and their values

curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
