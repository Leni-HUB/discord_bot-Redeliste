import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Set up bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Redeliste
redeliste = []

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='sprechen')
async def sprechen(ctx):
    user = ctx.author.name
    if user in redeliste:
        await ctx.send(f'{user}, du stehst bereits auf der Redeliste.')
    else:
        redeliste.append(user)
        await ctx.send(f'{user} wurde zur Redeliste hinzugefügt.')

@bot.command(name='weristdran')
async def weristdran(ctx):
    if redeliste:
        await ctx.send(f'Die nächste Person auf der Redeliste ist: {redeliste[0]}')
    else:
        await ctx.send('Die Redeliste ist leer.')

@bot.command(name='redeliste')
async def zeige_redeliste(ctx):
    if redeliste:
        liste = '\n'.join(f'{i+1}. {name}' for i, name in enumerate(redeliste))
        await ctx.send(f'🗣️ Aktuelle Redeliste:\n{liste}')
    else:
        await ctx.send('Die Redeliste ist aktuell leer.')

@bot.command(name='fertig')
async def fertig(ctx):
    user = ctx.author.name
    if redeliste and redeliste[0] == user:
        redeliste.pop(0)
        await ctx.send(f'Danke {user}, du wurdest von der Redeliste entfernt.')
    elif user in redeliste:
        await ctx.send(f'{user}, du bist nicht an der Reihe. Bitte warte, bis du dran bist.')
    else:
        await ctx.send(f'{user}, du bist nicht auf der Redeliste.')

# Run the bot
if __name__ == '__main__':
    bot.run(TOKEN)
