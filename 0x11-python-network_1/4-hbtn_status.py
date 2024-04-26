#!/usr/bin/python3
"""
This module fetches the status from the alx-intranet URL
using the requests package.
"""

import requests


if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
