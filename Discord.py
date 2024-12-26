import discord
from discord import app_commands
import random
import os
from dotenv import load_dotenv

intents = discord.Intents.all() # 権限
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# 起動時
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="占い"))
    print(f'{client.user}起動')
    await tree.sync() # スラッシュコマンドを同期

@tree.command(name="fortune", description="今日の運勢を占います")
async def fortune(interaction: discord.Interaction):
    fortunes = ["大吉", "吉", "中吉", "小吉", "末吉", "凶", "大凶"]
    message = f"あなたの今日の運勢は...{random.choice(fortunes)}です！"
    await interaction.response.send_message(message)
    print(f"/fortune\n{message}")

# 起動
load_dotenv()
TOKEN = os.environ.get('DISCORD_TOKEN')
client.run(TOKEN)
