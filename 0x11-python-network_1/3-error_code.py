#!/usr/bin/python3
"""
This module sends a request to a URL and displays the body of the response or
prints an error code if an HTTP error occurs.
"""

import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
