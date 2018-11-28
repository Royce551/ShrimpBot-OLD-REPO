#Import Modules
import discord
import asyncio
import logging
from discord.ext import commands
import random
import ShrimpConfig
import time

logging.basicConfig(level=logging.INFO)

client = discord.Client()
#Variables
Version = 'Shrimpbot 15.2'
uptimeA = time.time()

#Startup Message
timer = 0
@client.event
async def on_ready():
    print('Hello, user! Welcome to Shrimpbot! This is some information about me!')
    print('  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print('Username of what I am connected to.')
    print(client.user.name)
    print('My user ID.')
    print(client.user.id)
    print('  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print('Fully locked and loaded, let\'s do this!')
    await client.change_presence(game=discord.Game(name='I\'m a shrimp, and a bot. **| ' + Version))
    await client.edit_profile(password=None, username= '' + Version)
    
#Commands 

    @client.event
    async def on_message(message):
        if message.content.startswith('s:mes'):
            counter = 0
            tmp = await client.send_message(message.channel, 'Calculating messages...')
            async for log in client.logs_from(message.channel, limit=100):
                if log.author == message.author:
                    counter += 1

            await client.edit_message(tmp, 'You have sent {} messages since Shrimpbot started running.'.format(counter))

        elif message.content.startswith('s:cool'):
            coolname = message.content[len('$$cool'):].strip()
            await client.send_message(message.channel, 'Hmm, you seem like a cool individual!'.format(coolname))
    
        elif message.content.startswith('s:yep'):
            await client.send_message(message.channel, 'Nope!')
            print('Succesfully executed !yep.')

        elif message.content.startswith('s:help'):
            await client.send_message(message.channel, ''':information_source: **ShrimpBot Help | Updated 11/16/2018**
    
                :robot: **General** :robot:
                ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                **# s:messages** - Tells you how many messages you sent since Shrimpbot started.
                **s:cool** - Says that you are cool for self-gratification.
                **s:wait** - I\'ll just do nothing, literally, that's it. Boring, right?
                **s:yep and s:nope** - I'll say the opposite
                **#s:information** - Tells you information about me.
                **# s:useDM** -Makes me open a new DM with you so that you can use me in DM\'s.
                **s:countdown** - Counts down from 10.
                **# s:changelog** - Shows the changes made in the current and previous versions of
                                                Shrimpbot.
                **s:uptime** - Shows the time since ShrimpBot started in seconds.

                :performing_arts: **Roleplay** :performing_arts:
                ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                **s:pet \(someone)** - Pets someone.
                **s:hug \(someone)** - Hugs someone.
                **s:slap \(someone)** - Slaps someone.

                :video_game: **Games** :video_game:
                ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                **s:random \(number lower than 36)** - Shrimpbot picks a random number, if the number you
                pick matches it, you win! If not, you lose, obviously!
                *Note: Don't spam this command, please! You\'ll ratelimit the bot!*
                ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                Protip! You no longer have to type in the full command name of long commands! Commands
                with the "#" symbol do not need to be typed all the way. Simply type in the "s:" prefix and
                the first three characters.
                  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                ''')
            print('Executed !help.')

        elif message.content.startswith('s:nope'):
            await client.send_message(message.channel, 'Yes!')
            print('Executed !nope.')

        elif message.content.startswith('s:inf'):
            await client.send_message(message.channel, '''**ShrimpBot Information**
                ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━''')
            await client.send_message(message.channel, '**Version** - ' + Version + ''' Created using Python and discord.py by Squid Grill.
                This is licensed under the MIT license, feel free to do
                whatever you want with this.
                ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━''')
            await client.send_file(message.channel, 'ShrimpBanner.png')
            print('Executed s:information')
            

        elif message.content.startswith('s:use'):
            await client.send_message(message.channel, 'Alright, I\'m opening up a DM.')
            await client.send_message(message.author, 'Hello there! You can use me as normal here!')
        elif message.content.startswith('s:ping'):
            await client.send_message(message.channel, 'Pong! I am currently working, as you can clearly see!')
#Roleplay commands 
        elif message.content.startswith('s:fart'):
            fartname = message.content[len('$$fart'):].strip()
            await client.send_message(message.channel, 'Roleplay commands in Shrimpbot will be disabled until they can be properly fixed, sorry.'.format(fartname))

        elif message.content.startswith('s:pet'):
            petname = message.content[len('$$pet'):].strip()
            if '@everyone' in message.content:
                await client.send_message(message.channel, 'You can\'t ping everyone using Shrimpbot!')
            elif '@here' in message.content:
                await client.send_message(message.channel, 'You can\'t do a here ping using Shrimpbot!')
            else:
                await client.send_message(message.channel, '**{}**, you got patted by '.format(petname) + str(message.author) + '**.')
                await client.send_file(message.channel, 'petimage.png')

        elif message.content.startswith('s:kiss'):
            kissname = message.content[len('$$pet'):].strip()
            if '@everyone' in message.content:
                await client.send_message(message.channel, 'You can\'t ping everyone using Shrimpbot.')
            elif '@here' in message.content:
                await client.send_message(message.channel, 'You can\'t do a here ping using Shrimpbot.')
            else:
                await client.send_message(message.channel, 'Roleplay commands in Shrimpbot will be disabled until they can be properly fixed, sorry.'.format(kissname))

        elif message.content.startswith('s:slap'):
            slapname = message.content[len('$$slap'):].strip()
            if '@everyone' in message.content:
                await client.send_message(message.channel, 'You can\'t ping everyone using Shrimpbot!')
            elif '@here' in message.content:
                await client.send_message(message.channel, 'You can\'t do a here ping using Shrimpbot!')
            else:
                await client.send_message(message.channel, 'Ouch, **{}** got slapped by **'.format(slapname) + str(message.author) + '**.')
                await client.send_file(message.channel, 'slapimage.gif')
                                      
        elif message.content.startswith('s:hug'):
            hugname = message.content[len('$$hug'):].strip()
            if '@everyone' in message.content:
                await client.send_message(message.channel, 'You can\'t ping everyone using Shrimpbot!')
            elif '@here' in message.content:
                await client.send_message(message.channel, 'You can\'t do a here ping using Shrimpbot!')
            else:
                await client.send_message(message.channel, '**{}** got hugged by '.format(hugname) + str(message.author) + '**.')
                await client.send_file(message.channel, 'hugimage.gif')
            

        elif message.content.startswith('s:cou'):
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
            await client.edit_message(tmp, 'Zero! The timer is finished!'.format(countmessage))
        elif message.content.startswith('s:cha'):
            await client.send_message(message.channel, '''
                ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   
                **"Project: Make Shrimpbot less shit" changes**
               
                **Alpha 0.1.3**
                - Disabled all roleplay commands and other commands that allows the bot to send your own
                    message, this is to prevent abuse.
                - s:countdown no longer lets you send a reminder message. This, again, is to prevent abuse.
                - Improved formatting and general text on all information commands.
                - You no longer need to type the full name of long command names, you only need to type
                    the first 3 characters.
                - Removed the github link on the information panel. New releases of Shrimpbot will no
                    longer be on GitHub. DM me if you want to tell me about issues n\' stuff.
                - Some other minor internal changes.
                - Changed wording of some commands
                - Cleaned up code
                **Shrimpbot 14**
                - Minor Changes -
                **Shrimpbot 15** 
                - Roleplay commands have returned!
                - The bot will now send you a message if you try to run a command that it does not
                   recognize.
                - Many major security issues with the bot have been fixed.
                - Games have been added! The games currently available include **random**.
                - Menus in the bot, such as **help** now look nicer.
                  **Shrimpbot 15.1**
                - Added an uptime command and support for working with time.
                  **Shrimpbot 15.2** **Current Version!**
                - Fixed a bug that caused the uptime command to stop working when it tried to add days to
                  the counter.
                - Minor formatting change for **help**.
                ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                ''')
        elif message.content.startswith('s:testing'):
            if 'yes' in message.content:
                await client.send_message(message.channel, 'SUCCESS!' + Version)
                await client.send_file(message.channel, 'SakamotoAngary.png')
            else:
                await client.send_message(message.channel, 'SUCCESS BUT YES WASNT DETECTED!')
        elif message.content.startswith('s:random'):
            guessname = message.content[len('$$random '):].strip()
            randomnumber = str(random.randint(1,35))
            if guessname == randomnumber:
                await client.send_message(message.channel, ' :tada: **Great job! You are correct!**')
            else:
                await client.send_message(message.channel, ' :frowning2: Sorry, but you\'re wrong, the number was **' + str(randomnumber) + '**!')
        elif message.content.startswith('s:uptime'):
            seconds = round(time.time() - uptimeA)
            minutes = 0
            hours = 0
            days = 0
            while seconds >= 60:
                seconds -= 60
                minutes += 1
            
            while minutes >= 60:
                minutes -= 60
                hours += 1

            while hours >= 24:
                hours -= 24
                days += 1

            await client.send_message(message.channel, 'The bot has been running for ' + str(days) + ' days, ' + str(hours) + ' hours, ' + str(minutes) + ' minutes and ' + str(seconds) + ' seconds.')

        elif message.content.startswith('s:'):
                await client.send_message(message.channel, '''**This is not a command I recognize.**
                 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                 **Did you mistype something?** Type it again, then.
                 Some commands may have been removed between versions.
                 **If you're not sure what you can do with Shrimpbot,** you can see the full list of
                 commands by using **s:help**.
                 ''')
  
    

client.run('' + ShrimpConfig.token)
