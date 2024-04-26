#!/usr/bin/python3
"""
This script retrieves the last 10 commits from a given GitHub repository
and its owner, displaying each commit's SHA and the author's name.
"""

import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    response = requests.get(url)
    commits = response.json()

    for commit in commits[:10]:  # Limit to the last 10 commits
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author}")
