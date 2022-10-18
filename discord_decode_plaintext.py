"""
CSEC 791 MS Project
Grace Lombardi
Discord Covert Channel
Decode Plaintext
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
async def on_message(message: discord.Message):
    """
    Waits for a message that says "history" then checks for words from the military alphabet and
    decodes the message.
    """
    history = []
    hidden_message = []
    mil_alphabet = {'a': 'alpha', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo',
                    'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliet',
                    'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar',
                    'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
                    'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'xray', 'y': 'yankee',
                    'z': 'zulu'}
    if message.author == client.user:
        return
    if message.content.startswith('history'):

        channel = discord.utils.get(message.guild.text_channels, name="general")
        messages = channel.history(limit=500)
        async for message in messages:
            if not message.attachments:
                if message.author == client.user:
                    history.append(message.content)
    if history[0] == 'Boom!':
        for i in history[1:]:
            if i == 'Boom!':
                break
            hidden_message.append(i)
    unhidden_message = []
    for letter in hidden_message:
        for key, value in mil_alphabet.items():
            if letter == value:
                unhidden_message.append(key)
    unhidden_message = ''.join(unhidden_message)
    print("Message Successfully Decoded: ", unhidden_message[::-1])


def main():
    """
    This is the main decoding function.
    """
    client.run(discord_config.token)


if __name__ == '__main__':
    main()
