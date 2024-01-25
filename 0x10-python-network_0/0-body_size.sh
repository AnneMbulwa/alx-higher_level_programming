#!/bin/bash
# using curl to display the size of the response in bytes.
curl -s "$1" | wc -c
