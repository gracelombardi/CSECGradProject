"""
CSEC 791 MS Project
Grace Lombardi
Reddit Covert Channel
Decode Binary
"""
import re
import praw

import reddit_config


def authenticate():
    """
    This function authenticates to the reddit api.
    """
    reddit = praw.Reddit(client_id=reddit_config.client_id,
                         client_secret=reddit_config.client_secret,
                         user_agent=reddit_config.user_agent,
                         redirect_uri=reddit_config.redirect_uri,
                         refresh_token=reddit_config.refresh_token)
    return reddit


def main():
    """
    This is the main decoding function.
    """
    reddit = authenticate()
    binary = []
    submission_list = []
    submission = reddit.submission("dgx575")
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        submission_list.append(comment)
    for i in submission_list:
        comment = i.body
        if comment == 'I disagree!':
            binary.append('0')
        if comment == 'I agree!':
            binary.append('1')
        if comment == 'Boom!':
            binary.append('9')
    binary = ''.join(binary)
    binary_message = binary.split('9')
    history = re.findall('........', binary_message[-2])
    message = []
    for i in history:
        message.append(chr(int(i, 2)))
    message = ''.join(message)
    print("Message Successfully Decoded: ", message)


if __name__ == '__main__':
    main()
