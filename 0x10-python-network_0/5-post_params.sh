#!/bin/bash
# Sends a POST request to a URL with specified data fields and displays the body of the response.
curl -sX POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
