import os
import discord
from discord import app_commands
from datetime import datetime
import random
BERAT_ID = 244895648879607808
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

    if not os.path.exists("mesaj_gonderildi.txt"):
        berat = await client.fetch_user(BERAT_ID)

        await berat.send("askim seni cok seviyorum hayatima girdiginden beri her sey cok degisti kendimi yalniz hissetsem bile yanimda sen vardin. seninle gecirdigim tum anlar benim icin cok degerli ben bi daha birine karsi boyle hissedebilecegimi sanmiyorum sana cok ama cok asigim💞 umarim hep hayatimda olursun ve uep heraber oluruz sevgilim 222 💗")

        with open("mesaj_gonderildi.txt", "w") as f:
            f.write("gonderildi")

        print("Berat'a mesaj gönderildi!")
    else:
        print("Mesaj zaten gönderilmiş.")



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

token = os.getenv("DISCORD_TOKEN")
client.run(token)
