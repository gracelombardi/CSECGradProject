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
    username = input("Enter the username of the owner of the list: ")
    response = client.get_user(username=username)
    return response.data.id


def get_name_input():
    message = input("Enter the list name: ")
    return message


def main():
    message = []
    user_id = get_user_id()
    name = get_name_input()
    response = client.get_owned_lists(id=user_id)
    for i in response.data:
        if i.name == name:
            list_id = i.id
            response = client.get_list_members(id=list_id)
            for member in response.data:
                username = member.username
                letter = username[:1]
                message.append(letter)
            message = ''.join(message)
    print("Message Successfully Decoded: ", message)


if __name__ == '__main__':
    main()
