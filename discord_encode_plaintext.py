"""
CSEC 791 MS Project
Grace Lombardi
Discord Covert Channel
Encode Plaintext
"""
import discord

import discord_config

word_list = []
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    """
    Returns a message when there is a successful connection.
    """
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    """
    Waits for a message that says "hello" then sends words from the military alphabet to send the
    message.
    """
    if message.author == client.user:
        return

    if message.content.startswith('message'):
        for i in word_list:
            await message.channel.send(i)
        await message.channel.send("Boom!")


def get_message_input():
    """
    This function prompts the user for a message to encode and then returns a list of all characters
    in the message.
    """
    message = input("Enter the message to encode: ")
    message = message.replace(" ", "")
    chars = list(message.lower())
    return chars


def main():
    """
    This is the main encoding function.
    """
    mil_alphabet = {'a': 'alpha', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo',
                    'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliet',
                    'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar',
                    'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
                    'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'xray', 'y': 'yankee',
                    'z': 'zulu'}
    message = get_message_input()
    for i in message:
        letter = mil_alphabet[i]
        word_list.append(letter)
    client.run(discord_config.token)


if __name__ == '__main__':
    main()
