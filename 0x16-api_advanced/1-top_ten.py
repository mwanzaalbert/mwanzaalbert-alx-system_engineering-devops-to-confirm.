#!/usr/bin/python3
"""Demonstration of Reddit apis."""
import requests


def top_ten(subreddit):
    """Query the top ten subreddit."""
    # Define the headers to avoid 429 Too Many Requests error
    headers = {'User-Agent': 'Mozilla/5.0'}
    # Build the URL for the API request
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    # Make a GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful and not redirected
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Get the list of posts
        posts = data.get('data', {}).get('children', [])
        # Print the titles of the first 10 hot posts
        for post in posts[:10]:
            print(post.get('data', {}).get('title'))
    else:
        # Print None if the subreddit is invalid or redirected
        print(None)


if __name__ == "__main__":
    """Example Usage."""
    top_ten('programming')  # Should print top ten subreddit
    top_ten('this_is_a_fake_subreddit')  # Should print None
