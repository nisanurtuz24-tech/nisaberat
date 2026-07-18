import os
import discord
from discord import app_commands
from datetime import datetime
import random
intents = discord.Intents.default()

class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

client = MyClient()

@client.event
async def on_ready():
    print(f"Giriş yapıldı: {client.user}")

@client.tree.command(name="love", description="Nisa ve Berat ❤️")
async def love(interaction: discord.Interaction):
    embed = discord.Embed(
        title="💌 NisaKalpBerat'tan Mesaj",
        description="💖 **Nisa ve Berat birbirini çok seviyor.**\n\n🤍 Bu bot, sevginizi hatırlatmak için hazırlandı.",
        color=0xff69b4
    )

    await interaction.response.send_message(embed=embed)
@client.tree.command(name="days", description="Kaçıncı günümüz? 💕")
async def days(interaction: discord.Interaction):
    start_date = datetime(2026, 4, 19)
    today = datetime.now()

    day_count = (today - start_date).days + 1

    embed = discord.Embed(
        title="📅 NisaKalpBerat",
        description=(
            f"💖 Bugün birlikte **{day_count}. gününüz!**\n\n"
            "🎉 3. ay dönümünüze çok az kaldı! 🤍"
        ),
        color=0xff69b4
    )

    await interaction.response.send_message(embed=embed)
token = os.getenv("DISCORD_TOKEN")
@client.tree.command(name="love", ...)
async def love(...):
    ...

@client.tree.command(name="days", ...)
async def days(...):
    ...
    await interaction.response.send_message(embed=embed)


@client.tree.command(name="baby", description="Bebeğiniz nasıl olacak? 👶")
async def baby(interaction: discord.Interaction):
    chance = random.randint(1, 100)

    if chance <= 40:
        result = "👧 Bir kızınız olacak! 🎀"
    elif chance <= 80:
        result = "👦 Bir oğlunuz olacak! 💙"
    elif chance <= 95:
        result = "👶👶 Sürpriz! İkiz bebekleriniz olacak! 💞"
    else:
        result = "👶👶👶 İNANILMAZ! Üçüz bebekleriniz olacak! 🎉"

    embed = discord.Embed(
        title="🍼 NisaKalpBerat",
        description=f"{result}\n\n🤍 Umarız çok mutlu bir aileniz olur. 💖",
        color=0xff69b4
    )

    await interaction.response.send_message(embed=embed)

token = os.getenv("DISCORD_TOKEN")


client.run(token)
