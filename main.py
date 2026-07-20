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
        "gif": "https://tenor.com/tr/view/hello-kitty-dear-daniel-kiss-cute-gif-15829826"
    },
    {
        "song": "Bize Has",
        "artist": "Sibel Can",
        "gif": "https://tenor.com/tr/view/my-little-pony-twilight-sparkles-pinkie-pie-kiss-gif-14364376922814963375"
    },
    {
        "song": "Aşkım",
        "artist": "Bengü",
        "gif": "https://tenor.com/tr/view/kiss-kissing-lesbian-anime-strawberry-panic-gif-9155305389744741940"
    },
    {
        "song": "Dinle Beni Bi'",
        "artist": "Yüzyüzeyken Konuşuruz",
        "gif": "https://tenor.com/tr/view/renako-mai-kiss-kisses-freak-out-gif-13220785228267010349"
    },
    {
        "song": "Him & I",
        "artist": "G-Eazy & Halsey",
        "gif": "https://tenor.com/tr/view/lesbian-gif-22079307"
    },
    {
        "song": "Eskisi Gibi",
        "artist": "Lil Zey & Kozmos",
        "gif": "https://tenor.com/tr/view/ck006-aladdin-disney-toon-disney-jasmine-gif-8200920"
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
    music = random.choice(playlist)

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
client.run(token)
