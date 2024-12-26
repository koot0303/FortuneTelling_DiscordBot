import discord
from discord import app_commands
import random
import os
from dotenv import load_dotenv

intents = discord.Intents.all() # 権限
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

#起動時
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await tree.sync() # スラッシュコマンドを同期

@tree.command(name="fortune", description="今日の運勢を占います")
async def fortune(ctx: discord.Interaction):
    fortunes = ["大吉", "吉", "中吉", "小吉", "末吉", "凶", "大凶"]
    await interaction.response.send_message(f"あなたの今日の運勢は...{random.choice(fortunes)}です！")
    print("/fortune")

#起動
load_dotenv()
TOKEN=os.environ.get('DISCORD_TOKEN')
client.run(TOKEN)