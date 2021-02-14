import discord, datetime #모듈 불러오기
token = "ODEwMzUwMDg2ODYwMzA4NTAw.YCiXVA.uMXAwDj04vGAW6nrBwDSoni5sS0" #봇 토큰을 설정하기
client = discord.Client()

@client.event
async def on_ready():
    print("봇 준비 완료!")
    print(client.user)
    print("=========================")
    import asyncio
    user = len(client.users)
    server = len(client.guilds)
    await client.change_presence(status=discord.Status.offline)
    game = discord.Game("부팅 중...현재 명령어 사용 불가")
    message = [ str(user) + "명과" + str(server) + "개의 서버에서 활동중입니다!", "리버롤님이 저를 만들어주셨답니다!" ]
    while True:
        await client.change_presence(status=discord.Status.online, activity=discord.Game(message[0]))
        message.append(message.pop(0))
        await asyncio.sleep(5)

@client.event
async def on_member_join(member):
    await member.send(f'{member}님 저희 서버에 오신것을 환영합니다!')

@client.event
async def on_message(message):
    if message.content == "!하이즈 안녕":
        await message.channel.send("네 안녕하세요!")

    if message.content == "!디스코드":
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.red(), title="디스코드 링크", description="https://discord.gg/Sz9QMdcP8d")
        embed.set_image(url="https://blog.kakaocdn.net/dn/czSP7t/btqzvJKRgOb/eELJzLfuif31xD4QxkGVu0/img.jpg")
        embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content == '!내정보':
        user = message.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        await message.channel.send(f"{message.author.mention}의 가입일 : {date.year}/{date.month}/{date.day}")
        await message.channel.send(f"{message.author.mention}의 이름 / 아이디 / 닉네임 : {user.name} / {user.id} / {user.display_name}")
        await message.channel.send(message.author.avatar_url)

    if message.content.startswith(f"!채널메세지"):
        ch = client.get_channel(int(message.content[7:25]))
        await ch.send(message.content[26:])

    if message.content.startswith("!청소"):
        number = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=number)
        await message.channel.send(f"{number}개의 메세지가 삭제가 되었어요.")

    if message.content == "!딜레이테스트":
        await message.channel.send("딜레이 {0}초".format(bot.latency))

client.run(token)