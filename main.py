import disnake
import os
from disnake.ext import commands

bot = commands.Bot(command_prefix="*", intents=disnake.Intents.all())
token = "Your Token"

for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")

bot.run(token)
