#!/bin/bash
# displays all HTTP methods the server will accept using curl
curl -sI "$1" | grep -i 'Allow' | cut -d "" -f 2-
