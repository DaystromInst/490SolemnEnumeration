# 490 Solemn Enumeration by Jared Marriner
# Development began 5/13/2021
# kill me

import discord

TOKEN = 'XXXXXXXXXX'

client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    print('Greetings! I am 490 Solemn Enumeration!')
    print("I am the monitor of this installation!")


client.run(TOKEN)
