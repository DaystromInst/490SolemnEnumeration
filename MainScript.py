# 490 Solemn Enumeration by Jared Marriner
# Development began 5/13/2021
# kill me

import discord
import asyncio
import tokens

TOKEN = tokens.token

client = discord.Client()
server = client.guilds
channel_map = {}

# Things to think about: I feel uncomfy writing the banned slurs into the repo even though it's private/used to ban them

# Until then I guess I'll need to suck it up and hard code the no-nos
# May god have mercy on my soul
banned_words = ["nigger", "chink", "kike", "wetback", "spic"]


def mapChans():
    global channel_map
    global client

    servers = client.guilds

    for serv in servers:
        nom = serv.name
        chans = serv.text_channels
        channel_map.update({nom: chans})


def checkWord(msg: str):
    msgList = msg


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        # await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    global server
    global channel_map

    greet = 'Greetings! I am 490 Solemn Enumeration!\n'+"I am the monitor of this installation!"
    print(greet)

    for serv in server:
        key = serv.name
        chans = channel_map[key]
        target = chans[0]
        await target.send(greet)


client.run(TOKEN)
