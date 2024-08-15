#!/usr/bin/python3
"""Module to retrieve the number of subscribers
on a subreddit using Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """Function to get the number of subscribers on a subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'my-user-agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            return response.json().get("data", {}).get("subscribers", 0)
        except ValueError:
            return 0
    return 0
