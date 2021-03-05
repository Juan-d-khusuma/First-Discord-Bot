import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print(f"Bot is ready, username: {client.user}")

@client.event
async def on_message(message):
  if message.author == client.user:
    return None
  if message.content.startswith("$PING"):
    await message.channel.send("PONG!")
  
client.run(os.getenv("TOKEN"))
