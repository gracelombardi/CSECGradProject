import tweepy
import config

client = tweepy.Client(
    bearer_token=config.bearer_token,
    consumer_key=config.api_key,
    consumer_secret=config.api_secrets,
    access_token=config.access_token,
    access_token_secret=config.access_secret
)


def get_user_id():
    username = input("Enter the username of the profile to place your message on: ")
    response = client.get_user(username=username)
    return response.data.id


def get_message_input():
    message = input("Enter the message to encode: ")
    message = message.replace(" ", "")
    chars = list(message)
    return chars


def convert_to_binary(chars):
    binary = ''.join(format(ord(char), '08b') for char in chars)
    return binary


def main():
    user_id = get_user_id()
    response = client.get_users_tweets(id=user_id)
    message = get_message_input()
    binary = convert_to_binary(message)
    list_ids = []
    if len(response.data) < len(message):
        print("There are not enough tweets on this account to send the message. Please try a "
              "different user account.")
    else:
        for tweets in response.data:
            id = tweets.id
            list_ids.append(id)
        for num, id in zip(binary, list_ids):
            if num == '0':
                client.unlike(id)
            elif num == '1':
                client.like(id)
        print("Finished Liking/Unliking Tweets to Hide Message")


if __name__ == '__main__':
    main()
