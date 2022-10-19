"""
CSEC 791 MS Project
Grace Lombardi
Twitter Covert Channel
Decode Plaintext
"""
import base64
import hashlib
import os
import re
import tweepy
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session

import twitter_config


def authenticate():
    """
    This function authenticates with OAuth2 and returns the access_token.
    """
    redirect_uri = "https://ngrok.com"
    scopes = ["bookmark.read", "tweet.read", "users.read", "offline.access"]
    code_verifier = base64.urlsafe_b64encode(os.urandom(30)).decode("utf-8")
    code_verifier = re.sub("[^a-zA-Z0-9]+", "", code_verifier)
    code_challenge = hashlib.sha256(code_verifier.encode("utf-8")).digest()
    code_challenge = base64.urlsafe_b64encode(code_challenge).decode("utf-8")
    code_challenge = code_challenge.replace("=", "")
    oauth = OAuth2Session(twitter_config.client_id, redirect_uri=redirect_uri, scope=scopes)
    auth_url = "https://twitter.com/i/oauth2/authorize"
    authorization_url, state = oauth.authorization_url(
        auth_url, code_challenge=code_challenge, code_challenge_method="S256"
    )
    print(
        "Visit the following URL to authorize your App on behalf of your Twitter handle in a "
        "browser:"
    )
    print(authorization_url)
    authorization_response = input(
        "Paste in the full URL after you've authorized your App:\n"
    )
    token_url = "https://api.twitter.com/2/oauth2/token"
    auth = HTTPBasicAuth(twitter_config.client_id, twitter_config.client_secret)
    token = oauth.fetch_token(
        token_url=token_url,
        authorization_response=authorization_response,
        auth=auth,
        client_id=twitter_config.client_id,
        include_client_id=True,
        code_verifier=code_verifier,
    )
    return token['access_token']


def get_name_input():
    """
    This function prompts the user to enter a name for the Twitter list.
    """
    message = input("Enter a name for the list: ")
    return message


def main():
    """
    This is the main decoding function.
    """
    token = authenticate()
    client = tweepy.Client(token)
    mil_alphabet = {'a': 'alpha', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo',
                    'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliet',
                    'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar',
                    'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
                    'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'xray', 'y': 'yankee',
                    'z': 'zulu'}
    message = []
    bookmarks = client.get_bookmarks()
    for i in bookmarks:
        for tweet in i:
            word_list = str(tweet).split()
            word = word_list[0]
            for key, value in mil_alphabet.items():
                if word == value:
                    message.append(key)
    message = ''.join(message)
    print("Message Successfully Decoded: ", message[::-1])


if __name__ == '__main__':
    main()
