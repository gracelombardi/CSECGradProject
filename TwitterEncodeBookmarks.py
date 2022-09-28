import tweepy
from requests.auth import HTTPBasicAuth
import twitter_config
import base64
import hashlib
import os
import re
from requests_oauthlib import OAuth2Session


def authenticate():
    redirect_uri = "https://ngrok.com"
    scopes = ["bookmark.read", "bookmark.write", "tweet.read", "users.read", "offline.access"]
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


def get_message_input():
    message = input("Enter the message to encode: ")
    message = message.replace(" ", "")
    chars = list(message.lower())
    return chars


def get_name_input():
    message = input("Enter a name for the list: ")
    return message


def clear_bookmarks(client):
    bookmarks = client.get_bookmarks()
    if bookmarks.data is not None:
        for i in bookmarks.data:
            client.remove_bookmark(i.id)


def main():
    token = authenticate()
    client = tweepy.Client(token)
    message = get_message_input()
    clear_bookmarks(client)
    tweet_ids_list = []

    mil_alphabet = {'a': 'alpha', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo',
                    'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliet',
                    'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar',
                    'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
                    'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'xray', 'y': 'yankee',
                    'z': 'zulu'}

    for i in message:
        tweet_id = ''
        done = False
        list = client.search_recent_tweets(query=mil_alphabet.get(str(i)) + ' -is:retweet '
                                                                            '-is:reply '
                                                                            '-is:quote',
                                           max_results=10)
        word = mil_alphabet.get(str(i))
        token = list.meta['next_token']
        for tweet in list.data:
            if tweet is not None:
                word_list = str(tweet).split()
                if word_list[0] == word:
                    tweet_id = tweet.id
                    done = True
        while done is False:
            list = client.search_recent_tweets(query=mil_alphabet.get(str(i)) + ' -is:retweet '
                                                                                '-is:reply '
                                                                                '-is:quote',
                                               max_results=10, next_token=token)
            word = mil_alphabet.get(str(i))
            for tweet in list.data:
                if tweet is not None:
                    word_list = str(tweet).split()
                    if word_list[0] == word:
                        tweet_id = tweet.id
                        if tweet_id not in tweet_ids_list:
                            done = True
                        else:
                            token = list.meta['next_token']
                    else:
                        token = list.meta['next_token']
        print(tweet_id)
        tweet_ids_list.append(tweet_id)
        client.bookmark(tweet_id=tweet_id)
    print("Finished Bookmarking Tweets to Hide Message")


if __name__ == '__main__':
    main()
