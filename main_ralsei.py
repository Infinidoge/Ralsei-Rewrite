"""
------------------------------
Ralsei Base
Written by Infinidoge
------------------------------
Description:
    The base file from which Ralsei is constructed and run.
    This file will contain the Ralsei class, and is where base events, such as on_ready,
    and base commands, such as echo and shutdown, will be housed here.
------------------------------
List of officially supported cogs and their creators:
    - cog_random.py (Created by Infinidoge

List of officially supported utils and their creators:
    - config.py (Created by Infinidoge)
    - misc.py (Created by Infinidoge)
------------------------------
Contributors:
    - Infinidoge (Creator)
------------------------------
Misc Notes:
  1.If you majorly fix or create a feature, such as a cog, and the pull request was accepted,
    let Infinidoge on GitHub know, and your nae will be added to the contributors list.

  2.Doc strings for methods are formatted where anything within {} is a required argument,
    anything between [] is an optional argument, and options are represented with | between each option,
    within the above stated brackets.
"""

# ------------------------------
#            Imports

# Discord - provides an interface with discord to create a bot and allow it to function
import discord
import discord.ext.commands as commands

# Asyncio - utilities and pieces for asynchronous programming
import asyncio

# Dynamos
import core.dynamos.cog_dynamo as cog_dynamo
import core.dynamos.command_dynamo
from core.dynamos.event_dynamo import *

# Utils
from utils.config import Config
from utils.misc import *

# ------------------------------


class Ralsei(commands.Bot):
    """
    Ralsei Base Class
    ------------------------------
    Description:
        The Ralsei class, subclass of discord.ext.commands.Bot, is the home and main running class of Ralsei.
        When instantiated, this class requires that you provide an instance the Config class, (from utils.config)
        which will provide all of the needed information for the bot to run.
    ------------------------------
    Methods:
        ralsei.ralsei_run([token]):
            Takes the token provided from the Config provided during instantiation and starts the bot.
            Optionally, you may provide a different token to the start method, and it will use that token instead.
    """

    class BaseCommands:
        """
        Ralsei Base Class/Base Commands
        ------------------------------
        Description:
            Contains all of the basic commands of the bot.
            In your own version of the bot, you may add more base commands and they will automatically be loaded
        ------------------------------
        Commands:
          1.shutdown
                Shuts down the bot
          2.echo
                Echos the text input
        """

        def __init__(self, bot):
            self.bot = bot
            type(self).__name__ = 'Base Commands'

        @commands.command()
        @commands.is_owner()
        async def shutdown(self, ctx):
            """
            Shuts down Ralsei as a bot.
            Limited to Owner Only

            :param ctx:
            :return:
            """

            await ctx.channel.send("See ya!")
            await self.bot.close()
            print("Ralsei  |  Offline")

        # TODO: Add a restart command

        @commands.command()
        @commands.is_owner()
        async def echo(self, ctx, *, msg: str):
            """
            Echos the message sent
            Limited to Owner Only

            :param ctx:
            :param msg:
            :return:
            """

            await ctx.send(msg)
            await ctx.message.delete()

    @staticmethod
    def _dynamic_prefix(bot, msg):
        return bot.config.command_prefix

    def __init__(self, config=Config()):
        self.config = config

        self.dynamos = {"Events": EventDynamo(
            self,
            {},
            {}
        )}

        super(Ralsei, self).__init__(command_prefix=self._dynamic_prefix)

        self.add_cog(self.BaseCommands(self))

        for cls in [i.__getattribute__(get_func(i)[0]) for i in
                    (lambda z: [z.__getattribute__(x) for x in get_vars(z)])(
                        __import__("cogs", fromlist=[i[:len(i) - 3] for i in
                                                     get_files(self.config.cogs_dir)]))]:
            self.add_cog(cls(self))

    def ralsei_run(self, token=None):
        try:
            self.run(token if token is not None else
                     self.config.token if self.config.token is not None and self.config.token is not ""
                     else input("Temp Token:"))
        except Exception as e:
            print("An Exception occurred when trying to run Ralsei with that token:\n%s" % str(e))


ralsei = Ralsei()
ralsei.ralsei_run()
