#Import Libraries
import discord
import asyncio
import logging
from discord.ext import commands
import random


logging.basicConfig(level=logging.INFO)

client = discord.Client()
# Clock.


#Startup Events
timer = 0
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print('Locked and loaded, ready to go!')
    await client.change_presence(game=discord.Game(name='with python code | 0.1.1'))
    await client.edit_profile(password=None, username= 'ShrimpBot 0.1.1')
    
#Commands and their responses

    @client.event
    async def on_message(message):
        if message.content.startswith('s:messages'):
            counter = 0
            tmp = await client.send_message(message.channel, 'Calculating messages...')
            async for log in client.logs_from(message.channel, limit=100):
                if log.author == message.author:
                    counter += 1

            await client.edit_message(tmp, 'You have {} messages.'.format(counter))

        elif message.content.startswith('s:cool'):
            coolname = message.content[len('$$cool'):].strip()
            await client.send_message(message.channel, '{} seems like a cool individual!'.format(coolname))
    
          
        
        elif message.content.startswith('s:sleep'):
            await client.send_message(message.channel, 'Alright, I\'m sleeping')
            await asyncio.sleep(5)
            await client.send_message(message.channel, 'Done sleeping')
            print('Succesfully executed !sleep.')
        
        elif message.content.startswith('s:yep'):
            await client.send_message(message.channel, 'Nope!')
            print('Succesfully executed !yep.')

        elif message.content.startswith('s:help'):
            await client.send_message(message.channel, '''**ShrimpBot Help | Updated 9/22/2017**
                !messages - Check how many messages you have
                !cool - Tell someone who's cool.
                !sleep - Makes me sleep for a few moments
                !yep and !nope - I'll say the opposite
                !information - Tells information about me
                !useprivate - Makes me send you a DM so that you can use me in PM's.
                !notify - Ping someone
                !fart (Name) - Tells someone they farted
                !pet (Name) - Pets someone.
                !countdown [Reminder] - Counts down from 10 with the reminder specified.
                ''')
            print('Succesfully executed !yep.')

        elif message.content.startswith('s:nope'):
            await client.send_message(message.channel, 'Yes!')
            print('Succesfully executed !nope.')

        elif message.content.startswith('s:die'):
            await logout()

        elif message.content.startswith('s:information'):
            await client.send_message(message.channel, '''**ShrimpBot Information**
                **Version** - 0.1.1 Alpha
                Created using Python and discord.py with no additional libraries
                by Squid Grill.
                This bullshit is licensed under the MIT license, feel free to do
                whatever the hell you want with this, but don't blame me if
                something goes wrong.
                **Github** - https://github.com/Royce551/TestBot
                =========================================================
                ''')

        elif message.content.startswith('s:useprivate'):
            await client.send_message(message.channel, 'Alright, I\'m sending you a DM.')
            await client.send_message(message.author, 'Hello there! DM me the commands, same way you do normally, aight?')

        elif message.content.startswith('s:notify'):
            notifyname = message.content[len('$$notify'):].strip()
            await client.send_message(message.channel, '{}, someone needs you!'.format(notifyname))

        elif message.content.startswith('s:getpins'):
            counter = 0
            tmp = await client.send_message(message.channel, 'Please wait.')
            async for message in client.logs_from(message.channel, limit=100):
                if channel.pins == message.channel:
                    counter +=1

            await client.edit_message(tmp, 'There are {} pings.'.format(counter))

        elif message.content.startswith('s:ping'):
            await client.send_message(message.channel, 'Pong! I am currently working, as you can clearly see!')

        elif message.content.startswith('s:fart'):
            fartname = message.content[len('$$fart'):].strip()
            await client.send_message(message.channel, 'Ew, {}, you farted! https://i.ytimg.com/vi/IPUfhcL7Tfo/hqdefault.jpg'.format(fartname))

        elif message.content.startswith('s:pet'):
            petname = message.content[len('$$pet'):].strip()
            await client.send_message(message.channel, 'Looks like someone-()- is getting petted! [http://bit.ly/2BeTpND] (too lazy to do any embedded messages)'.format(petname))
        elif message.content.startswith('s:clear'):
            await client.delete_messages(message.channel)
        elif message.content.startswith('s:kiss'):
            kissname = message.content[len('$$pet'):].strip()
            await client.send_message(message.channel, 'Love is in the air! {} is getting kissed! Ooo!! [http://bit.ly/2yYpUdb]'.format(kissname))
        elif message.content.startswith('s:slap'):
            slapname = message.content[len('$$kiss'):].strip()
            await client.send_message(message.channel, '{} got slapped! Must\'ve hurt, I wonder why they got slapped... [http://bit.ly/2BN5Hfu]'.format(slapname))
        elif message.content.startswith('s:hug'):
            hugname = message.content[len('$$hug'):].strip()
            await client.send_message(message.channel, 'That\'s cute! {} is being hugged, how adorable. [http://bit.ly/2D8t7d4]'.format(hugname))
            

        elif message.content.startswith('s:countdown'):
            countmessage = message.content[len('$$countdown'):].strip()
            tmp = await client.send_message(message.channel, '10!')
            await asyncio.sleep(1)
            await client.edit_message(tmp, '9!')
            await asyncio.sleep(1)
            await client.edit_message(tmp, '8!')
            await asyncio.sleep(1)
            await client.edit_message(tmp, '7!')
            await asyncio.sleep(1)
            await client.edit_message(tmp, '6!')
            await asyncio.sleep(1)
            await client.edit_message(tmp, '5!')
            await asyncio.sleep(1)
            await client.edit_message(tmp, '4!')
            await asyncio.sleep(1)
            await client.edit_message(tmp, '3!')
            await asyncio.sleep(1)
            await client.edit_message(tmp, '2!')
            await asyncio.sleep(1)
            await client.edit_message(tmp, '1!')
            await asyncio.sleep(1)
            await client.edit_message(tmp, 'Zero! The timer for "{}" is finished!'.format(countmessage))
        elif message.content.startswith('s:changelog'):
            await client.send_message(message.channel, '''ShrimpBot 0.1.1 Changelog
                - Added a couple of new roleplay related commands
                - Improved text and typography across various places.
                =================================================================================
                ''')
        elif message.content.startswith('s:say'):
            saymessage = message.content[len('$$say'):].strip()
            await client.send_message(message.channel, '{}'.format(saymessage))
    
#This is the bot's token
client.run('MzUxNTEwMDc1NTg1ODU1NDk4.DRiGIg.pXdnQmSFiVB3hv2OX0lkHE7q9mM')
