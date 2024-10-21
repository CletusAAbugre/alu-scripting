#!/usr/bin/python3
"""
This module contains the function top_ten.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.

    If the subreddit is invalid, print "None".
    """
    # Define the base URL and headers
    url = 'https://www.reddit.com/r/{}/hot/.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        # Make the request and avoid redirects
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check for status code 200 (OK)
        if response.status_code != 200:
            print("None")
            return

        # Parse the JSON response
        data = response.json()
        
        # Check if the 'data' and 'children' keys exist in the JSON response
        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            
            # Loop through the posts and print their titles
            for post in posts:
                print(post['data']['title'])
        else:
            print("None")
    except requests.exceptions.RequestException:
        print("None")
    except ValueError:
        print("None")


if __name__ == "__main__":
    # Use this function in another script or for testing.
    pass

