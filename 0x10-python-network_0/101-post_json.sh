#!/bin/bash
# This script sends a JSON POST request with the contents of a file and displays the response body.
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
