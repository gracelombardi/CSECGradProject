"""
CSEC 791 MS Project
Grace Lombardi
Discord Covert Channel
Decode Binary
"""
import re
import discord
from discord.ext import commands

import discord_config


intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    """
    Returns a message when there is a successful connection.
    """
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    """
    Waits for a message that says "history" then checks for thumbs up or thumbs down and decodes
    the message.
    """
    history = []
    if message.author == client.user:
        return
    if message.content.startswith('history'):
        channel = discord.utils.get(message.guild.text_channels, name="general")
        messages = channel.history(limit=500)
        async for message in messages:
            if not message.attachments:
                thumbsup = [x for x in message.reactions if
                         str(x.emoji) == '👍']  # replace the emoji with the one you want
                thumbsdown = [x for x in message.reactions if
                            str(x.emoji) == '👎']  # replace the emoji with the one you want
                if thumbsup:
                    history.append('1')
                if thumbsdown:
                    history.append('0')
    mes = []
    binary = ''.join(history)
    history = re.findall('........', binary)
    for i in history:
        mes.append(chr(int(i, 2)))
    decoded_message = ''.join(mes)
    print("Message Successfully Decoded: ", decoded_message)


def main():
    """
    This is the main decoding function.
    """
    client.run(discord_config.token)


if __name__ == '__main__':
    main()
