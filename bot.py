import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True  # Important for message content access

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}!")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

if __name__ == "__main__":
    TOKEN = os.getenv("BOT_TOKEN")
    if not TOKEN:
        print("Error: No BOT_TOKEN found in environment variables.")
    else:
        bot.run(TOKEN)
