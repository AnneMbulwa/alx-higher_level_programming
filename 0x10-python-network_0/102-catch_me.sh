#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me that causes the server to
# respond with a message containing You got me!

curl -sX PUT -H "Origin: HorbertonSchool" -d "User_Id=98" 0.0.0.0:5000/catch_me
