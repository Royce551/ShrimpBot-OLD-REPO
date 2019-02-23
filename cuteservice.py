import discord
import random
from discord.ext import commands
#CuteService Ver. 1, Patch 0.
def cuver():
    return 'Version 1 Patch 1'
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
def help(page):
    helpsend = 'p'
    if page == 'test':
        helpsend = 'test complete'
        return helpsend
