#!/usr/bin/python3
"""Demonstration of Reddit apis."""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Query all hot articles."""
    if hot_list is None:
        hot_list = []

    # Define the headers to avoid 429 Too Many Requests error
    headers = {'User-Agent': 'Mozilla/5.0'}
    # Build the URL with the after parameter for pagination
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'after': after} if after else {}

    # Make a GET request to the Reddit API
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # Check if the request was successful and not redirected
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json().get('data', {})
        # Append the titles of the current page's posts to the hot_list
        posts = data.get('children', [])
        hot_list.extend([post.get('data', {}).get('title') for post in posts])

        # Get the next page's "after" value
        after = data.get('after')
        # If there's another page, recurse
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        # Return None if the subreddit is invalid or redirected
        return None


if __name__ == "__main__":
    """Example Usage."""
    result = recurse("programming")
    print(len(result))

    result = recurse("this_is_a_fake_subreddit")
    print(result)
