#!/usr/bin/python3
"""Demonstration of Reddit apis."""
import requests


def count_words(subreddit, word_list, after=None, word_count=None):
    """Words counter."""
    if word_count is None:
        # Initialize a dictionary to keep track of word counts
        word_count = {word.lower(): 0 for word in word_list}

    # Define headers to avoid 429 Too Many Requests error
    headers = {'User-Agent': 'Mozilla/5.0'}
    # Build URL with the after parameter for pagination
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'after': after} if after else {}

    # Make a GET request to the Reddit API
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # Check if the request was successful and not redirected
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json().get('data', {})
        # Get the list of posts
        posts = data.get('children', [])

        # Iterate over each post to extract and count keywords in the title
        for post in posts:
            title = post.get('data', {}).get('title', '').lower().split()
            for word in title:
                if word in word_count:
                    word_count[word] += 1

        # Get the next page's "after" value
        after = data.get('after')

        # If there's another page, recurse
        if after:
            return count_words(subreddit, word_list, after, word_count)
        else:
            # Sort and print the word count
            sorted_words = sorted(word_count.items(),
                                  key=lambda item: (-item[1], item[0]))
            for word, count in sorted_words:
                if count > 0:
                    print(f"{word}: {count}")

    else:
        # If the subreddit is invalid or redirected, return nothing
        return


if __name__ == "__main__":
    # Example usage:
    count_words('programming',
                ['react', 'python', 'java', 'JaVa' 'javascript',
                 'scala', 'no_results_for_this_one'])
