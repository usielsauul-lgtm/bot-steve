import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="Steve ", intents=intents)

@bot.event
async def on_ready():
    print("✅ ¡Conectado exitosamente!")

@bot.command()
async def hola(ctx):
    await ctx.send("Hola mundo")
    
bot.run(TOKEN)
