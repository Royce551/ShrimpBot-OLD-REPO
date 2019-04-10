import discord
import random
from discord.ext import commands
#CuteService Ver. 1, Patch 0.
def cuver():
    return 'Version 1 Patch 2'
def cute():
    cutenumber = str(random.randint(1,16))
    cutesend = 'p'
    if cutenumber == '1':
        cutesend = 'cute1.png'
    elif cutenumber == '2':
        cutesend = 'cute2.png'
    elif cutenumber == '3':
        cutesend = 'cute3.png'
    elif cutenumber == '4':
        cutesend = 'cute4.png'
    elif cutenumber == '5':
        cutesend = 'cute5.png'
    elif cutenumber == '6':
        cutesend = 'cute6.png'
    elif cutenumber == '7':
        cutesend = 'cute7.png'
    elif cutenumber == '8':
        cutesend = 'cute8.png'
    elif cutenumber == '9':
        cutesend = 'cute9.png'
    elif cutenumber == '10':
        cutesend = 'cute10.png'
    elif cutenumber == '11':
        cutesend = 'cute11.png'
    elif cutenumber == '12':
        cutesend = 'cute12.jpg'
    elif cutenumber == '13':
        cutesend = 'cute13.png'
    elif cutenumber == '14':
        cutesend = 'cute14.png'
    elif cutenumber == '15':
        cutesend = 'cute15.png'
    elif cutenumber == '16':
        cutesend = 'cute16.jpg'
    return cutesend

def hug():
    hugsend = 'p'
    huginfo = 'p'
    hugnumber = str(random.randint(1,1))
    if hugnumber == '1':
        hugsend = 'hug1.png'
        huginfo = '''
         ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
By うさみん | https://twitter.com/usamin1211/status/1079953811702042624'''
        return hugsend, huginfo;

def slap():
    slapsend = 'p'
    slapinfo = 'p'
    slapnumber = str(random.randint(1,1))
    if slapnumber == '1':
        slapsend = 'slapimage.gif'
        slapinfo = '''
         ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sources not available, sorry \:('''
        return slapsend, slapinfo;

def pet():
    petsend = 'p'
    petinfo = 'p'
    petnumber = str(random.randint(1,1))
    if petnumber == '1':
        petsend = 'petimage.png'
        petinfo = '''
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sources not available, sorry \:('''
        return petsend, petinfo;

def help(page):
    helpsend = 'p'
    if page == 'changelog':
        helpsend = '''**changelog**
        s:changelog (page number)
        Lists all the most recent changes to Shrimpbot.
        Page 1 - Shrimpbot 16x
        Page 2 - Shrimpbot 15x
        Page 3 - Shrimpbot 14 and 13.'''
        return helpsend
    elif page == 'cute':
        helpsend = '''**cute**
        s:cute
        Gives you a random cute picture (usually anime).'''
        return helpsend
    elif page == 'useDM':
        helpsend = '''**useDM**
        s:useDM
        Opens a direct message with the user.
        Note - You can also simply right click the bot and select "Message".
        # This command does not need to be typed in all the way!'''
        return helpsend
    elif page == 'information':
        helpsend = '''**information**
        Gives you information about the bot, including version number of the bot itself and the cute service, and
        a link to a page about the license the bot uses, and credits for people who helped with the bot.'''
        return helpsend
   #elif page == 'cool':
       #helpsend = '''**cool**
        #Says that you are cool.'''
       #return helpsend
    elif page == 'messages':
        helpsend = '''**messages**
        Gives you a count of all messages you sent in the channel you executed the command in since the bot started running, up to an arbitrairy limit of 100.
        # This command does not need to be typed in all the way!'''
        return helpsend


