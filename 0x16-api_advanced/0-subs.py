#!/usr/bin/python3
"""
Module that query the Reddit API and returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102\
            Safari/537.36"
    }
    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    return 0
