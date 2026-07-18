import os
import discord

intents = discord.Intents.default()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Giriş yapıldı: {client.user}')

token = os.getenv("DISCORD_TOKEN")

client.run(token)