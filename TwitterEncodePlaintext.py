import tweepy
import string
import random
import config

client = tweepy.Client(
    bearer_token=config.bearer_token,
    consumer_key=config.api_key,
    consumer_secret=config.api_secrets,
    access_token=config.access_token,
    access_token_secret=config.access_secret
)


def get_message_input():
    message = input("Enter the message to encode: ")
    message = message.replace(" ", "")
    chars = list(message)
    return chars


def get_name_input():
    message = input("Enter a name for the list: ")
    return message


def generate_random_word(first_letter):

    lowercase_letters = string.ascii_lowercase
    number = random.randint(4, 10)
    word = ''
    if first_letter is not None:
        word += first_letter
    while len(word) != number:
        word += random.choice(lowercase_letters)
    return word


def main():
    message = get_message_input()
    name = get_name_input()
    list = client.create_list(name=name)
    list_id = list.data['id']
    for i in message:
        word = generate_random_word(i)
        username = client.get_users(usernames=word)
        while username.data is None:
            word = generate_random_word(i)
            username = client.get_users(usernames=word)
        user_id = username.data[0].id
        client.add_list_member(id=list_id, user_id=user_id)
    print("Finished Creating List to Hide Message")


if __name__ == '__main__':
    main()
