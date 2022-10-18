"""
CSEC 791 MS Project
Grace Lombardi
Discord Covert Channel
Encode Binary
"""
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
    Waits for a message that says "message" then removes all reactions then adds thumbs up or
    thumbs down to signify binary.
    """
    mes = get_message_input()
    binary = convert_to_binary(mes)
    print(binary)
    if message.author == client.user:
        return
    if message.content.startswith('message'):
        channel = discord.utils.get(message.guild.text_channels, name="general")
        messages = channel.history(limit=500)
        async for message in messages:
            for reaction in message.reactions:
                await message.clear_reaction(reaction)
        limit = len(binary)
        messages = channel.history(limit=limit)
        binary = list(binary)
        message_length = len(binary)
        ind_num = 0
        while ind_num < (message_length - 1):
            async for message in messages:
                binary_number = binary[ind_num]
                if binary_number == '0':
                    print('dislike')
                    await message.add_reaction('👎')
                if binary_number == '1':
                    print('like')
                    await message.add_reaction('👍')
                ind_num += 1


def get_message_input():
    """
    This function prompts the user for a message to encode and then returns a list of all characters
    in the message.
    """
    message = input("Enter the message to encode: ")
    message = message.replace(" ", "")
    chars = list(message.lower())
    return chars


def convert_to_binary(chars):
    """
    This function coverts every character in the list to their binary equivalent.
    """
    binary = ''.join(format(ord(char), '08b') for char in chars)
    return binary


def main():
    """
    This is the main encoding function.
    """
    client.run(discord_config.token)


if __name__ == '__main__':
    main()
