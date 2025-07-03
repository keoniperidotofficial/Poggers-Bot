import discord
from discord import app_commands
from discord.ext import commands
import os

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} slash command(s).")
    except Exception as e:
        print(f"Error syncing commands: {e}")

@bot.tree.command(name="say", description="Make the bot speak!")
@app_commands.describe(text="What should the bot say?")
async def say(interaction: discord.Interaction, text: str):
    await interaction.response.send_message(text)

bot.run(os.getenv("BOT_TOKEN"))
