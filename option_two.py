import discord
import logging
from discord.ext import commands
import random
from prettytable import PrettyTable

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord_two.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


bot = commands.Bot(command_prefix='?')
player_list = []
notify_list = []

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

#---- commands ----
    
@bot.command()
async def tenmans(ctx, player: discord.Member=None):
    if (await check_length(ctx)): #adding more than one player???
        if player == None: #no extra parameter
            await ctx.send(str(ctx.author) + " has joined!")
            player_list.append(ctx.author)
        else:
            await ctx.send(str(player) + " has been added!")
            player_list.append(player)
        await ctx.send(str(10 - len(player_list)) + " spot(s) left")
    if (10 - len(player_list) < 1):
        await shuffle(ctx)
        await notify_players(ctx)

@bot.command(name='shuffle')
async def reshuffle(ctx):
    await shuffle(ctx)

@bot.command()
async def remove(ctx, member: discord.Member=None):
    if member == None:
        person = ctx.author
    else:
        person = member
        
    player_list.remove(person)
    notify_list.remove(person)
    await ctx.send("Removed " + str(person) + " from the lobby.")
    
@bot.command()
async def showlist(ctx):
    '''displays the lobby in a pretty table'''
    table = PrettyTable()
    table.add_column("Players", await concatenize_players(player_list))
    await ctx.send("```" + table.get_string() + "```")

@bot.command()
async def clear(ctx):
    '''clears the lobby'''
    player_list.clear()
    notify_list.clear()
    await ctx.send("Clearing player lobby...")

@bot.command()
async def notifyme(ctx):
    notify_list.append(ctx.author)
    await ctx.send("I'll let you know when the game is starting")

#---- helper functions ----
async def check_length(ctx): #False = too many people
    '''checking if there's too many people in list'''
    if len(player_list) >= 10:
        await ctx.send("Sorry bud, there's too many people")
        return False
    else:
        return True

async def concatenize_players(player_list):
    '''converts Member models to strings'''
    string_list = []
    for player in player_list:
        string_list.append(str(player))
    return string_list

async def check_list(ctx, member):#true = is in lobby already
    '''checks if player is in lobby already'''
    for player in player_list:
        if member == player:
            await ctx.send("You're already in the lobby")
            return True 
    return False

async def shuffle(ctx): #might be good to check if lobby is full or not
    '''puts players into teams'''
    str_players = await concatenize_players(player_list)
    random.shuffle(str_players)
    team_one = []
    team_two = []
    
    for x in range(len(str_players)):
        if x < 5:
            team_one.append(str_players[x])
        else:
            team_two.append(str_players[x])

    table = PrettyTable()
    table.add_column("Team 1", team_one)
    table.add_column("Team 2", team_two)
    table.align = "c"

    result = table.get_string(title="T E N M A N S")
    print(result)
    await ctx.send("Here are the teams\n```" + result + "```")

async def notify_players(ctx):
    mention_str = ""
    for player in notify_list:
        mention_str += " " + player.mention
    await ctx.send("The game is ready" + mention_str)
    
bot.run('NTIyNDU4Mzk2NjI5MjcwNTMx.DvLRJA.L1O1cqEIylU8WqVSA2EEDyl3htw')
