import discord
from discord.ext import commands
import random
import os
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot(
        intents=discord.Intents.all(),  # 全てのインテンツを利用できるようにする
        activity=discord.Game("Discord Bot入門"),  # "**をプレイ中"の"**"を設定,
)

#起動時
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command(name="占い", description="今日の運勢を占います")
async def fortune(ctx):
    fortunes = ["大吉", "吉", "中吉", "小吉", "末吉", "凶", "大凶"]
    await ctx.respond(f"あなたの今日の運勢は...{random.choice(fortunes)}です！")

#起動
load_dotenv()
os.environ.get('DISCORD_TOKEN')
bot.run('DISCORD_TOKEN')