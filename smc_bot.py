import discord
import datetime
import os
import youtube_dl
import requests
from bs4 import BeautifulSoup
import re
from discord.ext import commands

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    game = discord.Game("!도움말")
    await client.change_presence(status=discord.Status.online, activity=game)

'''
오류 해결 중..(아시는 분은 디스코드 Carn1val#6974로 부탁드릴게요.)

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 656053252277796864:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
        if payload.emoji.name == 'one':
            role = discord.utils.get(guild.roles, name='1학년')
        elif payload.emoji.name == 'two':
            role = discord.utils.get(guild.roles, name='2학년')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
                print("완료.")
            else:
                print("유저를 찾을 수 없습니다.")
        else:
            print("역할을 찾을 수 없습니다.")
@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 656053252277796864:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
        if payload.emoji.name == 'one':
            role = discord.utils.get(guild.roles, name='1학년')
        elif payload.emoji.name == 'two':
            role = discord.utils.get(guild.roles, name='2학년')
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove.roles(role)
                print("완료.")
            else:
                print("유저를 찾을 수 없습니다.")
        else:
            print("역할을 찾을 수 없습니다.")
'''


@client.event
async def on_reaction_add(reaction, user):
    if str(reaction.emoji) == ":lock:":
        await reaction.message.channel.send(user + "보안과에 대해 설명하겠습니다. ```스마트보안솔루션과 \n 교육목표 : 프로그램 및 정보통신에 대한 기본적인 지식을 바탕으로 정보보호에 대한 개방적 문제를 해결할 수 있는 창의적이고 능동적인 능력을 갖추어서, 해킹이나 바이러스 등의 보안 위협에 능동적으로 대처할 수 있는 인력을 양성합니다.```")


@client.event
async def on_message(message):
    if message.author.bot:
        return None

    id = message.author.id

    if message.content.startswith('!안녕'):
        await message.channel.send("안녕하세요")

    if message.content.startswith("!test"):
        embed = discord.Embed(title="테스트", description="test!!!", color=0x00ff00, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text="테스트 종료")
        await message.channel.send(embed=embed)

    if message.content.startswith("!도움말"):
        embed = discord.Embed(title="도움말", description="```!도움말 \n!안녕 \n!젊은 \n!학교소개 \n!로고 \n!교가 \n!전경 \n!상징 \n!현재시간```"
                              , color=0x00ff00, timestamp=datetime.datetime.utcnow())

        embed.set_footer(text="세명컴퓨터고등학교")
        await message.channel.send(embed=embed)

    if message.content.startswith("!안녕"):
        embed = discord.Embed(title="", description="<@{0}> 학생아 안녕".format(id), color=0x00ff00,
                              timestamp=datetime.datetime.utcnow())
        embed.set_footer(text="세명컴퓨터고등학교")
        await message.channel.send(embed=embed)

    if message.content.startswith("!젊은"):
        embed = discord.Embed(title="젊은", description="독수리", color=0x00ff00, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text="완벽했다")
        await message.channel.send(embed=embed)

    if message.content.startswith("!학교소개"):
        embed = discord.Embed(title="세명컴퓨터고등학교",
                              description="교훈 : '성신예(誠信禮)를 바탕으로 애국(愛國)하는 사람이 되자. \n개교 : 1974년 4월 29일 \n유형 : 특성화고등학교"
                                          "\n성별 : 남여공학 \n운영 형태 : 사립 \n학교 법인 : 세명학원"
                                          "\n교장 : 남송옥 \n교감 : \n학생 수 : 606명 (남 529명 / 여 77명)(2016/4/1 기준) \n교직원 수 : 64명 (남 37명 / 여 27명)"
                                          "(2016/4/1 기준) \n관할 교육청 : 서울특별시교육청"
                                          "\n소재지 : 서울특별시 은평구 불광동 \n공식홈페이지 : http://www.smc.hs.kr/"
                                          "\n공식블로그 : https://blog.naver.com/semyeongcom "
                                          "\n카카오플러스친구 : https://pf.kakao.com/_pLaxcu", color=0x00ff00,
                              timestamp=datetime.datetime.utcnow())
        embed.set_footer(text="세명컴퓨터고등학교")
        await message.channel.send(embed=embed)

    if message.content.startswith("!로고"):
        embed = discord.Embed(title="세명컴퓨터고등학교 로고", description="", color=0x00ff00,
                              timestamp=datetime.datetime.utcnow())
        embed.set_footer(text="세명컴퓨터고등학교")
        embed.set_image(url="http://image.classting.com/s3/images/classting/1494566837746084_320.jpg")
        await message.channel.send(embed=embed)

    if message.content.startswith("!교가"):
        embed = discord.Embed(title="세명컴퓨터고등학교 교가", description="", color=0x00ff00,
                              timestamp=datetime.datetime.utcnow())
        embed.set_footer(text="세명컴퓨터고등학교")
        embed.set_image(url="http://www.smc.hs.kr/crosseditor/binary/images/2018/02/06/20180206153122552_HJUUUIUO.jpg")
        await message.channel.send(embed=embed)

    if message.content.startswith("!전경"):
        embed = discord.Embed(title="세명컴퓨터고등학교 전경", description="", color=0x00ff00,
                              timestamp=datetime.datetime.utcnow())
        embed.set_footer(text="세명컴퓨터고등학교")
        embed.set_image(
            url="https://ww.namu.la/s/fc55f54c7b378f50f2e5cf702712a73f192a60f84ebe364e666d9be4049f6222c52a3344e6aea9ec81c512fdb92d44670ed6d60d90f62b425e0fca95420c93e999334ce86a02e0fce41ab5488ed8bae495f9510e3f57a2c9b83b1bb5128d9c08")
        await message.channel.send(embed=embed)

    if message.content.startswith("!상징"):
        embed = discord.Embed(title="세명컴퓨터고등학교 상징", description="", color=0x00ff00,
                              timestamp=datetime.datetime.utcnow())
        embed.set_footer(text="세명컴퓨터고등학교")
        embed.set_image(url="http://www.smc.hs.kr/crosseditor/binary/images/2016/10/27/20161027180416506_Y00G69TZ.png")
        await message.channel.send(embed=embed)

    if message.content.startswith("!현재시간"):
        embed = discord.Embed(title="현재시간은  ", description="{0}".format(datetime.datetime.utcnow()) + "입니다",
                              color=0x00ff00, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text="세명컴퓨터고등학교")
        await message.channel.send(embed=embed)

    if message.content.startswith("!모두모여"):
        await message.channel.send("@everyone")

    if message.content.startswith("!등교"):
        embed = discord.Embed(title="등교", description="닉네임 : <@{0}>".format(id), color=0x00ff00,
                              timestamp=datetime.datetime.utcnow())
        embed.set_footer(text="등교 시간 ")
        await message.channel.send(embed=embed)
    if message.content.startswith("!하교"):
        embed = discord.Embed(title="하교", description="닉네임 : <@{0}>".format(id), color=0xff0000,
                              timestamp=datetime.datetime.utcnow())
        embed.set_footer(text="하교 시간 ")
        await message.channel.send(embed=embed)

    if message.content.startswith("!학과소개"):
        embed = discord.Embed(title="세명컴퓨터고등학교 학과소개", description="아래에 이모지를 추가하면 학과소개를 합니다. \n 🔒 : 보안과 \n 📱 : 디바이스과 \n 🤖 : 인공지능과 \n 🎮 : 게임과", color=0x00ff00,
                              timestamp=datetime.datetime.utcnow())
        embed.set_footer(text="세명컴퓨터고등학교")
        await message.channel.send(embed=embed)


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
