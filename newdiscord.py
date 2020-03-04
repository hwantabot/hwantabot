import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("문의 받는중!")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("환타샵 가격은?"):
        await message.channel.send("임펄스:5만,3.5만,2만,1만 / 황금벙커 1만,2만 / 패키지 상품가격 + 추가 구매 가격 5천 / 개별 상품 가격 5천 ```자세한건 디스코드 대리 가격표 확인바람.```")
    if message.content.startswith("환타샵 문의는?"):
            await message.channel.send("개인DM,카카오톡: https://open.kakao.com/o/ssvwThSb")
    if message.content.startswith("환타샵 핵 종류는?"):
        await message.channel.send("```임펄스VIP사용중!(디스터브드 추가예정)```")


client.run("Njg0NjgzOTU4MjMxMTA1NTgz.Xl9rtQ.ocEcVabkKGiNDONevGn2LsZHccg")