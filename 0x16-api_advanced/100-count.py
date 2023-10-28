#!/usr/bin/python3
"""
Query Reddit API, count & sort hot article titles with keywords
"""

import re
import requests


def count_words(subreddit, word_list, after='', word_dict={}):
    """
    Query Reddit API, count & sort hot article titles with keywords
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json().get('data')
    if data is None:
        return None
    children = data.get('children')
    if children is None or len(children) == 0:
        return None
    for child in children:
        title = child.get('data').get('title').lower()
        for word in word_list:
            word = word.lower()
            if re.search(rf'\b{word}\b', title):
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1
    after = data.get('after')
    if after is None:
        if len(word_dict) == 0:
            return None
        for key, value in sorted(word_dict.items(),
                                 key=lambda x: (-x[1], x[0])):
            print(f'{key}: {value}')
        return word_dict
    return count_words(subreddit, word_list, after, word_dict)
