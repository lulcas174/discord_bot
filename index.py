from discord.ext import commands
from dotenv import load_dotenv
import os
from discord import Intents
from cep_commands import get_cep
import gettext

from cotation_commands import get_dollar_cotation, get_euro_cotation
from holidays_commands import get_holidays

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
intents = Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} está online')


@bot.command()
async def dollar(context):
    rate = await get_dollar_cotation()
    await context.send(f"A taxa de câmbio atual do dólar para o real é de  {rate:.2f}.")


@bot.command()
async def euro(context):
    rate = await get_euro_cotation()
    await context.send(f"A taxa de câmbio atual do euro para o real é de  {rate:.2f}.")


@bot.command()
async def converter_dolar(context, value: float):
    try:
        rate = await get_dollar_cotation()
        await context.send(f"O valor de {value} dólares em reais é de R${rate * float(value):.2f}.")
    except:
        await context.send("Ocorreu um erro ao processar o comando.")


@converter_dolar.error
async def converter_dolar_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Você precisa informar o valor a ser convertido.")


@bot.command()
async def converter_euro(context, value: float):
    try:
        rate = await get_euro_cotation()
        await context.send(f"O valor de {value} euros em reais é de R${rate * value:.2f}.")
    except:
        await context.send("Ocorreu um erro ao processar o comando.")


@converter_euro.error
async def converter_euro_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Você precisa informar o valor a ser convertido.")


@bot.command()
async def cep(context, cep):
    try:
        cep = await get_cep(cep)
        await context.send(
            f"O CEP {cep['cep']} está localizado em {cep['city']}, {cep['state']} e o nome da rua é {cep['address']}, do bairro {cep['district']}.")
    except Exception as e:
        await context.send(f'Ocorreu um erro ao processar o cep: {e}')

@bot.command()
async def feriados(context, year):
    try:
        holidays = await get_holidays(year)
        holidays_list = holidays['response']['holidays']

        for holiday_information in holidays_list:
            holiday = {
                'name': holiday_information['name'],
                'country': holiday_information['country']['name'],
                'date': holiday_information['date']['iso']
            }
            await context.send(f"O feriado {holiday['name']} acontece no {holiday['country']} no dia {holiday['date']}")
    except Exception as e:
        await context.send(f'Ocorreu um erro ao processar o ano: {e}')



bot.run(TOKEN)
