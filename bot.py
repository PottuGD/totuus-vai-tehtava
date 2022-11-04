import discord
from discord.ext import commands
import random
from choices import truths, dares


intents = discord.Intents.all()
client = commands.Bot(command_prefix='.', intents=intents)


@client.event
async def on_ready():
    print("bot ready")

@client.command()
async def ping(ctx):
    await ctx.send("pong")

@client.command(aliases=['to'])
async def totuus(ctx):

    user = client.get_user(ctx.message.author.id)
    profilePicture = user.avatar.url

    view = discord.ui.View(timeout=None)
    buttonSign1 = discord.ui.Button(label="🎭 Totuus", style=discord.ButtonStyle.green)
    buttonSign2 = discord.ui.Button(label="⚒ Tehtävä", style=discord.ButtonStyle.red)
    buttonSign3 = discord.ui.Button(label="🎲 random", style=discord.ButtonStyle.blurple)

    embed = discord.Embed(title="**Totuus**", description=random.choice(truths), color=0xf50505)
    embed.set_author(name=f"{user} pyysi totuuden:", icon_url=profilePicture)
    embed.set_footer(text="paina 🎭 jos haluat Auden totuuden. paina ⚒ jos haluat uuden tehtävän")

    async def buttonSign_callback1(interaction):
        await totuus(ctx)

    async def buttonSign_callback2(interaction):
        await tehtävä(ctx)

    async def buttonSign_callback3(interaction):
        await randomq(ctx)


    buttonSign1.callback = buttonSign_callback1
    buttonSign2.callback = buttonSign_callback2
    buttonSign3.callback = buttonSign_callback3

    view.add_item(item=buttonSign1)
    view.add_item(item=buttonSign2)
    view.add_item(item=buttonSign3)

    await ctx.send(embed=embed, view=view)

@client.command(aliases=['te'])
async def tehtävä(ctx):

    user = ctx.message.author
    profilePicture = user.avatar.url

    view = discord.ui.View(timeout=None)
    buttonSign1 = discord.ui.Button(label="🎭 Totuus", style=discord.ButtonStyle.green)
    buttonSign2 = discord.ui.Button(label="⚒ Tehtävä", style=discord.ButtonStyle.red)
    buttonSign3 = discord.ui.Button(label="🎲 random", style=discord.ButtonStyle.blurple)

    embed = discord.Embed(title="**Tehtävä**", description=random.choice(dares), color=0xf50505)
    embed.set_author(name=f"{user} pyysi tehtävän", icon_url=profilePicture)
    embed.set_footer(text="paina 🎭 jos haluat uuden totuuden. paina ⚒ jos haluat uuden tehtävän.")

    async def buttonSign_callback1(interaction):
        await totuus(ctx)

    async def buttonSign_callback2(interaction):
        await tehtävä(ctx)

    async def buttonSign_callback3(interaction):
        await randomq(ctx)

    buttonSign1.callback = buttonSign_callback1
    buttonSign2.callback = buttonSign_callback2
    buttonSign3.callback = buttonSign_callback3

    view.add_item(item=buttonSign1)
    view.add_item(item=buttonSign2)
    view.add_item(item=buttonSign3)

    await ctx.send(embed=embed, view=view)

@client.command(aliases=['ra', 'r', 'random'])
async def randomq(ctx):
    if random.randint(0, 1) == 0:
        await totuus(ctx)
    else:
        await tehtävä(ctx)

@client.command(aliases=['ee'])
async def ehdotaEmbed(ctx):
    embed = discord.Embed(title="**Ehdota kysymyksiä tai tehtäviä**",
                          description="Ehdota kysymyksiä tai tehtäviä meidän omalle totuus vai tehtävä botille!",
                          color=0xf40606)
    embed.add_field(name="Esimerkki ehdotus 1:", value="Totuus: Onko sinulla ihastusta?", inline=True)
    embed.add_field(name="Esimerkki ehdotus 2:", value="Tehtävä: Lyö itseäsi 5 kertaa.", inline=True)

    await ctx.send(embed=embed)


client.run('MTAzNzYyMzE0NTI0MDIxNTYwMg.GWCds0.qyDtrA2TIr3sGpkFtQH8du5lI5OhUULc-Qsc_k')
