#!/usr/bin/python3
"""Retrieving top 10 posts from a subreddit"""
import requests


def top_ten(subreddit):
    """A method to query a given API and return the top 10 hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "my-user-agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            all_posts = response.json().get("data", {}).get("children", [])
            for count, post in enumerate(all_posts[:10]):
                print(post.get("data", {}).get("title"))
        except ValueError:
            print("None")
    else:
        print("None")
