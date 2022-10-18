"""
CSEC 791 MS Project
Grace Lombardi
Reddit Covert Channel
Decode Binary
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
    This is the main decoding function.
    """
    reddit = authenticate()
    comment_ids = []
    binary = []
    for comment in reddit.redditor('lombardig').comments.new(limit=None):
        comment_ids.append(comment.id)
    for comment_id in comment_ids:
        comment = reddit.comment(comment_id)
        if comment.score == 1:
            binary.append('0')
        if comment.score == 2:
            binary.append('1')
    binary = ''.join(binary)
    message = chr(int(binary, 2))
    print("Message Successfully Decoded: ", message)


if __name__ == '__main__':
    main()
