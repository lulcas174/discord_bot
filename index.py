import requests
from discord.ext import commands
from dotenv import load_dotenv
import os
import json
from discord import Intents

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
intents = Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} está online')

@bot.command()
async def dollar(ctx):
    rate = get_dollar_cotation()
    await ctx.send( f"A taxa de câmbio atual do dólar para o real é de  {rate:.2f}.")

def get_dollar_cotation():
    url = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
    response = requests.get(url)
    data = json.loads(response.text)
    return float(data["USDBRL"]["bid"])


bot.run(TOKEN)
