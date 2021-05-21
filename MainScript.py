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
banned_words = [""]


async def roleCheck(place):
    found = False
    roles = place.roles
    for spot in roles:
        if spot.name == "Cryptum":
            found = True
            break

    if not found:
        perms = discord.Permissions(send_messages=False,stream=False,change_nickname=False,administrator=False)
        await place.create_role("Cryptum", perms, reason="Protocol dictates I apprehend and assign this restraint to those who misbehave.")


async def mapChans():
    global channel_map
    global client

    servers = client.guilds

    for serv in servers:
        nom = serv.name
        chans = serv.text_channels
        channel_map.update({nom: chans})


async def checkWord(msg: str, author, serv):
    msgStr = msg.split()
    found = False

    for word in msgStr:
        word = word.lower()
        for slur in banned_words:
            if word == slur:
                print('UNACCEPTABLE')
                found = True
                break
        if found:
            break

    # Do punishment stuff in here
    if found:
        roleCall = author.roles

        for thing in roleCall:
            await author.remove_roles(thing)

        roleCall = await serv.fetch_roles()

        for thing in roleCall:
            if thing.name == "Cryptum":
                await author.add_roles(thing, "Protocol dictates action!")
                break

    # What do for pyunishmunchen?
    # Perhaps track strikes in JSON dict
    # Create jail role and store the time of the strike in the JSON
    # 3 strikes and kick. Simple as.
    # Stikes can expire. Once time served, remove jail role.
    # Maybe remember the user on kick. If they return, ban instead of kick


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        print("message detected")
        return

    await checkWord(message.content.lower(), message.author, message.guild)  # probe for slurs


@client.event
async def on_ready():
    global server
    global channel_map
    await mapChans()

    greet = 'Greetings! I am 490 Solemn Enumeration!\n'+"I am the monitor of this installation!"
    print(greet)

    for serv in server:
        key = serv.name
        greet2 = 'Greetings! I am 490 Solemn Enumeration!\n' + "I am the monitor of installation \""+key+"\"!"

        chans = channel_map[key]
        target = chans[0]
        await target.send(greet2)

        await roleCheck(serv)


client.run(TOKEN)
