import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os

TOKEN = 'ODgxMzI3MDQ5MzYzNTYyNTA2.YSrNxg.42Fgpz-9VWthPLD5220EauwbfB0'
BOT_PREFIX = '-'

bot = commands.Bot(command_prefix=BOT_PREFIX)

@bot.event
async def on_ready():
    print("Přihlášen jako: " + bot.user.name + "\n")


@bot.command(pass_context=True, aliases=['j', 'joi'])
async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    await voice.disconnect()

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f"The bot has connected to {channel}\n")

    await ctx.send(f"Připojen {channel}")


@bot.command(pass_context=True, aliases=['l', 'lea'])
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f"The bot has left {channel}")
        await ctx.send(f"Odpojen {channel}")
    else:
        print("Bot was told to leave voice channel, but was not in one")
        await ctx.send("Bot se odpojil, nikdo tu není :(")


@bot.command(pass_context=True)
async def zpravabotovijasny(ctx):
   channel = bot.get_channel(798949416484077608)
   await channel.send('Kdyby někdo chtěl je možnost používat našeho bota pro songy atd, sice není tak kvalitní jako např. groovy ale snad poslouží Commandy: -join -play ODKAZ -leave')


@bot.command(pass_context=True)
async def jakmocjematogay(ctx):
   channel = bot.get_channel(863555433666707496)
   await channel.send('Mato je velkej gay')


@bot.command(pass_context=True)
async def botodstavkax(ctx):
   channel = bot.get_channel(881447068462358578)
   await channel.send('Bot bude neaktivní od 10:00 do 23:00 - Vylepšení a oprava chyb')


@bot.command(pass_context=True)
async def jakmocjeteflongay(ctx):
   channel = bot.get_channel(863555433666707496)
   await channel.send('Teflon je transexual')


@bot.command(pass_context=True)
async def papiryna363(ctx):
   channel = bot.get_channel(863555433666707496)
   await channel.send('Papíry na 363 lze získat u Sama')

  


@bot.command(pass_context=True)
async def damo(ctx):
   channel = bot.get_channel(863555433666707496)
   await channel.send('Praotec cech, boh')


@bot.command(pass_context=True)
async def minus(ctx):
   channel = bot.get_channel(863555433666707496)
   await channel.send('bayside vie')   


@bot.command(pass_context=True)
async def damone(ctx):
   channel = bot.get_channel(842436516860002314)
   await channel.send('Ne')


@bot.command(pass_context=True)
async def damonene(ctx):
   channel = bot.get_channel(842438599953743924)
   await channel.send('Ne')   


@bot.command(pass_context=True)
async def damogutgut(ctx):
   channel = bot.get_channel(842436516860002314)
   await channel.send('Gut Gut')


@bot.command(pass_context=True)
async def odkazdamoweb(ctx):
   channel = bot.get_channel(863555433666707496)
   await channel.send('https://www.damova-tvorba-do-railworks.cz/')


@bot.command(pass_context=True)
async def invite(ctx):
   channel = bot.get_channel(842436516860002314)
   await channel.send('https://discord.gg/KFUdtGEQnH')


@bot.command(pass_context=True, aliases=['p', 'pla'])
async def play(ctx, url: str):

    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            print("Removed old song file")
    except PermissionError:
        print("Trying to delete song file, but it's being played")
        await ctx.send("ERROR: Hudba se momentálně přehrává, nebud jako Martin")
        return

    await ctx.send("Stahuji soubory, počkejte prosím. Při větších souborech či delších videích, muže trvat stahování trochu déle. Toto je ovšem dočasné, omluvte to prosím :)")

    voice = get(bot.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloading audio now\n")
        ydl.download([url])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            print(f"Renamed File: {file}\n")
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: print("Song done!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07

    nname = name.rsplit("-", 2)
    await ctx.send(f"Přehrává se: {nname[0]}")
    print("playing\n")


bot.run(TOKEN)