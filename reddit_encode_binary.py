"""
CSEC 791 MS Project
Grace Lombardi
Reddit Covert Channel
Encode Binary
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


def get_message_input():
    """
    This function prompts the user for a message to encode and then returns a list of all characters
    in the message.
    """
    message = input("Enter the message to encode: ")
    message = message.replace(" ", "")
    chars = list(message)
    return chars


def convert_to_binary(chars):
    """
    This function coverts every character in the list to their binary equivalent.
    """
    binary = ''.join(format(ord(char), '08b') for char in chars)
    return binary


def upvote_comment(reddit, comment_id):
    """
    This function upvotes a specific comment based on the comment id.
    """
    comment = reddit.comment(comment_id)
    print("Score before upvoting : " + str(comment.score))
    comment.upvote()
    print("Score after upvoting : " + str(comment.score))


def downvote_comment(reddit, comment_id):
    """
    This function downvotes a specific comment based on the comment id.
    """
    comment = reddit.comment(comment_id)
    print("Score before downvoting : " + str(comment.score))
    comment.downvote()
    print("Score after downvoting : " + str(comment.score))


def main():
    """
    This is the main encoding function.
    """
    message = get_message_input()
    binary = convert_to_binary(message)
    reddit = authenticate()
    submission = reddit.submission("dgx575")
    for binary_number in binary:
        if binary_number == '0':
            comment = "I disagree!"
            submission.reply(body=comment)
        if binary_number == '1':
            comment = "I agree!"
            submission.reply(body=comment)

    submission.reply(body='Boom!')
    print("Finished Adding Comments to Hide Message")


if __name__ == '__main__':
    main()
