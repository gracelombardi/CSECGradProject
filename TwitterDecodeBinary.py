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
    username = input("Enter the username of the profile to retrieve message from: ")
    response = client.get_user(username=username)
    return response.data.id


def convert_to_binary(chars):
    binary = ''.join(format(ord(char), '08b') for char in chars)
    return binary


def main():
    user_id = get_user_id()
    response = client.get_users_tweets(id=user_id)
    binary = []
    list_ids = []
    for tweets in response.data:
        id = tweets.id
        list_ids.append(id)
    for id in list_ids:
        likes = client.get_liking_users(id=id)
        if likes.data is None:
            binary.append('0')
        else:
            for i in likes.data:
                if str(i) == "lombardi_grace":
                    binary.append('1')
    binary = ''.join(binary)
    message = chr(int(binary, 2))
    print("Message Successfully Decoded: ", message)


if __name__ == '__main__':
    main()
