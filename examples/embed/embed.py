import discord
from discord.ext import commands

from zakilla.embed_create import EmbedCreator

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def embed_setup(ctx):
    view = EmbedCreator(ctx)
    await ctx.send(embed=view.get_default_embed, view=view)

bot.run("YOUR_BOT_TOKEN")