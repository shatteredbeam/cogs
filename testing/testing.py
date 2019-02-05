import discord
from discord.ext import commands


class TestCog:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def respond(self, user: discord.member):
        await self.bot.say(f"I can respond, {user.mention}")


def setup(bot):
    bot.add_cog(TestCog(bot))

