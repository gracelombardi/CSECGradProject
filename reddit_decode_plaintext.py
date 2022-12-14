"""
CSEC 791 MS Project
Grace Lombardi
Reddit Covert Channel
Decode Plaintext
"""

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
    This is the main encoding function.
    """
    reddit = authenticate()
    mil_alphabet = {'a': 'alpha', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo',
                    'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliet',
                    'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar',
                    'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
                    'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'xray', 'y': 'yankee',
                    'z': 'zulu'}
    message = []
    submission_list = []
    submission = reddit.submission("dgx575")
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        submission_list.append(comment)
    for i in submission_list:
        comment = i.body
        word_list = str(comment).split()
        word = word_list[0]
        for key, value in mil_alphabet.items():
            if word == value:
                message.append(key)
    message = ''.join(message)
    print("Message Successfully Decoded: ", message)


if __name__ == '__main__':
    main()
