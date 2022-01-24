import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    hitchhiker_quotes = [
        'There is an art, it says, or rather, a knack to flying. The knack lies in learning how to throw yourself at the ground and miss.',
        'It is a mistake to think you can solve any major problems just with potatoes.',
        'In the beginning the Universe was created. This has made a lot of people very angry and been widely regarded as a bad move.',
        'A common mistake that people make when trying to design something completely foolproof is to underestimate the ingenuity of complete fools.',
    ]

    if message.content == 'towel!':
        #response = random.choice(brooklyn_99_quotes)
        response = random.choice(hitchhiker_quotes)
        await message.channel.send(response)

    #assignment additions:

    abe_quotes = [
            "With malice toward none with charity for all with firmness in the right as God gives us to see the right let us strive on to finish the work we are in to bind up the nation's wounds, to care for him who shall have borne the battle and for his widow and his orphan ~ to do all which may achieve and cherish a just and lasting peace among ourselves and with all nations.",
            "Fourscore and seven years ago our fathers brought forth, on this continent, a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal.",
            "It is rather for us to be here dedicated to the great task remaining before us—that from these honored dead we take increased devotion to that cause for which they here gave the last full measure of devotion—that we here highly resolve that these dead shall not have died in vain—that this nation, under God, shall have a new birth of freedom, and that government of the people, by the people, for the people, shall not perish from the earth.",
            "We must not be enemies. Though passion may have strained, it must not break our bonds of affection. The mystic chords of memory will swell when again touched, as surely they will be, by the better angels of our nature.",
            ]

    if message.content == 'Abe!':
        response = random.choice(abe_quotes)
        await message.channel.send(response)


client.run(TOKEN)
