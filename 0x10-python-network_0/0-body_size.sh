#!/bin/bash
# This script sends a request to a URL and displays the size of the body of the response in bytes.
curl -sI "$1" | wc -c
