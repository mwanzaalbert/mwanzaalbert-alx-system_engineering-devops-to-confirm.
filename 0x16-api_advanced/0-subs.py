#!/usr/bin/python3
"""Demonstration of Reddit apis."""
import requests


def number_of_subscribers(subreddit):
    """Query total No. of Subscribers."""
    # Define headers to avoid 429 Too Many Requests error
    headers = {'User-Agent': 'Mozilla/5.0'}
    # Build the URL for the API request
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Make a GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful and not redirected
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json().get('data', {})
        # Return the number of subscribers
        return data.get('subscribers', 0)
    else:
        # Return 0 if the subreddit is invalid or redirected
        return 0


if __name__ == "__main__":
    """Example Usage."""
    print(number_of_subscribers('programming'))  # Should print all subscribers
    print(number_of_subscribers('this_is_a_fake_subreddit'))  # Should print 0
