"""
CSEC 791 MS Project
Grace Lombardi
Twitter Covert Channel
Decode Binary
"""
import tweepy
import re

import twitter_config

client = tweepy.Client(
    bearer_token=twitter_config.bearer_token,
    consumer_key=twitter_config.api_key,
    consumer_secret=twitter_config.api_secret,
    access_token=twitter_config.access_token,
    access_token_secret=twitter_config.access_secret
)


def get_user_id():
    """
    This function prompts the user for a username and then returns the user id associated with that
    username.
    """
    username = input("Enter the username of the profile to retrieve message from: ")
    response = client.get_user(username=username)
    return response.data.id


def main():
    """
    This is the main decoding function.
    """
    user_id = get_user_id()
    response = client.get_users_tweets(id=user_id, max_results=100)
    binary = []
    list_ids = []
    for tweets in response.data:
        tweet_id = tweets.id
        list_ids.append(tweet_id)
    for tweet_id in list_ids:
        likes = client.get_liking_users(id=tweet_id)
        if likes.data is None:
            binary.append('0')
        else:
            for i in likes.data:
                if str(i) == "lombardi_grace":
                    binary.append('1')
    mes = []
    binary = ''.join(binary)
    print(binary)
    history = re.findall('........', binary)
    for i in history:
        mes.append(chr(int(i, 2)))
    decoded_message = ''.join(mes)
    print("Message Successfully Decoded: ", decoded_message)


if __name__ == '__main__':
    main()
