from zakilla.embed_create import EmbedCreator
from discord import Embed

import discord

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot(command_prefix="!", intents=intents)

@bot.command()
async def embed_setup(ctx):
    embed = Embed(
        title="Sample Embed",
        description="This is a sample embed created using EmbedCreator.",
        color=discord.Color.blue()
    )

    embed_creator = EmbedCreator(ctx=ctx, embed=embed)
    message = await embed_creator.start()

bot.run("YOUR_BOT_TOKEN")