import discord
from discord.ext import commands
import os
import asyncio
from captcha.image import ImageCaptcha
import random
import urllib
from urllib.request import Request
import bs4
from bs4 import BeautifulSoup
from urllib import parse


client = discord.Client()

@client.event
async def on_ready():
    print('봇이 로그인 하였습니다.')
    print(' ')
    print('닉네임 : {}'.format(client.user.name))
    print('아이디 : {}'.format(client.user.id))
    while True:
        user = len(client.users)
        server = len(client.guilds)
        messages = ["HELLO!", "I BOT MADE  FOR#1234" , "봇 건의는" , str(user) + "My name is using my bot on OPEN 1 day.", str(server) + "에 제 봇이 있다구요!"]
        for (m) in range(5):
            await client.change_presence(status=discord.Status.online, activity=discord.Activity(name=messages[(m)], type=discord.ActivityType.watching))
            await asyncio.sleep(4)

@client.event
async def on_message(message):
    if message.content.startswith("안녕하세요"):
        await message.channel.send(f"<@!{message.author.id}>좋은 한국어 인사 예절이네요 ! 보기 좋아요")

@client.event
async def on_member_join(member):
    try:
        syscha = member.guild.system_channel
        await syscha.send(f"{member.mention} Welcome! Good day! Welcome to OPEN 1day. 😀")
    except:
        pass

@client.event
async def on_member_remove(member):
    try:
        syscha = member.guild.system_channel
        await syscha.send(member.name + "OH MY GOD ``" + member.guild.name + "`` GOOD BYE SEE YOU NEXT TIME")
    except:
        pass




client.run('NzQ2Mzg0NjAwMTEyMDM4MDE0.Xz_i0w.Zz5gLkH1sP-TRwXwCcb7WUZZiCI')