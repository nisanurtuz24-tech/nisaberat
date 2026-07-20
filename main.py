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

playlist_songs = [
    {
        "song": "Herkesim",
        "artist": "Aqtaii",
        "gif": "https://c.tenor.com/cA57Eoie-wYAAAAd/tenor.gif"
    },
    {
        "song": "Bize Has",
        "artist": "Sibel Can",
        "gif": "https://media1.tenor.com/m/5o4mBp6ppKIAAAAd/ck006-aladdin.gif"
    },
    {
        "song": "Aşkım",
        "artist": "Bengü",
        "gif": "https://media.gifdb.com/hello-kitty-daniel-kiss-3ip9w41r7cw1d55s.gif"
    },
    {
        "song": "Dinle Beni Bi'",
        "artist": "Yüzyüzeyken Konuşuruz",
        "gif": "https://media.gifdb.com/strawberry-panic-kiss-5x6z8v3p0s.gif"
    },
    {
        "song": "Him & I",
        "artist": "G-Eazy & Halsey",
        "gif": "https://media.gifdb.com/anime-girls-kiss-l4bqg1u5j.gif"
    },
    {
        "song": "Eskisi Gibi",
        "artist": "Lil Zey & Kozmos",
        "gif": "https://media.gifdb.com/pinkie-pie-kiss-hug-r1m4v8l2.gif"
    }
]

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

@client.tree.command(name="baby", description="Bebeğiniz nasıl olacak? 👶")
async def baby(interaction: discord.Interaction):
    results = [
        "👧 Bir kızınız olacak! 🎀",
        "👦 Bir oğlunuz olacak! 💙",
        "👶👶 İkiz bebekleriniz olacak! 💕",
        "👶👶👶 Üçüz bebekleriniz olacak! 🎉",
        "👶👶👶👶 Dördüz bebekleriniz olacak! 🤯",
        "🏳️‍⚧️ Çocuğunuz trans doğdu!",
        "🏳️‍🌈 Çocuğunuz lezboş doğdu! 😭"
    ]

    result = random.choice(results)

    embed = discord.Embed(
        title="🍼 NisaKalpBerat",
        description=result,
        color=0xff69b4
    )
    await interaction.response.send_message(embed=embed)
@client.tree.command(name="playlist", description="🎧 Size özel bir şarkı önerir.")
async def playlist(interaction: discord.Interaction):
    music = random.choice(playlist_songs)

    embed = discord.Embed(
        title="🎧 Our Playlist",
        color=0xff69b4
    )

    embed.add_field(
        name="Now Playing",
        value=f"🎵 **{music['song']}**\n👤 *{music['artist']}*",
        inline=False
    )

    embed.set_image(url=music["gif"])

    await interaction.response.send_message(embed=embed)
token = os.getenv("DISCORD_TOKEN")
print(f"Token bulundu mu? {token is not None}")
client.run(token)
