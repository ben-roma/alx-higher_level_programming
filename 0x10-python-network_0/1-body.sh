#!/bin/bash
# This script sends a GET request to a URL and displays the body of a 200 status code response.
curl -s -L -f "$1" -X GET
