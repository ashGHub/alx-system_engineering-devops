#!/usr/bin/python3
"""
Module that query the Reddit API and prints
the titles of the first 10 hot posts
"""

import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102\
            Safari/537.36"
    }
    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code == 200:
        for i in range(10):
            list = response.json().get("data").get("children")
            if (i < len(list)):
                child_data = list[i]
                print(child_data.get("data").get("title"))
    else:
        print(None)
