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

    class BaseEvents:
        """
        Ralsei Base Class/Base Events
        ------------------------------
        Description:
            Contains all of the basic events of the bot.
            In your own version of the bot, you may add more events and they will automatically be loaded
        ------------------------------
        Events:
          1.on_ready
                Prints basic readout information when the bot is ready and active.
        """

        def __init__(self, bot):
            self.bot = bot
            type(self).__name__ = 'Base Events'

        def __events__(self):
            [self.bot.event(getattr(self, i)) for i in get_func(self)]

        async def on_ready(self):
            print("Ralsei  |  Online")
            print("-------------------------")
            print("| Logged in as:         |")
            print("|  %s               |" % self.bot.user.name)
            print("|-----------------------|")
            print("| Id: %s|" % self.bot.user.id)
            print("-------------------------")

    @staticmethod
    def _dynamic_prefix(bot, msg):
        return bot.config.command_prefix

    def __init__(self, config=Config()):
        self.config = config

        super(Ralsei, self).__init__(command_prefix=self._dynamic_prefix)

        self.add_cog(self.BaseCommands(self))

        self.BaseEvents(self).__events__()

    def ralsei_run(self, token=None):
        try:
            self.run(token if token is not None else
                     self.config.token if self.config.token is not None and self.config.token is not ""
                     else input("Temp Token:"))
        except Exception as e:
            print("An Exception occurred when trying to run Ralsei with that token:\n%s" % str(e))


ralsi = Ralsei()
ralsi.ralsei_run()
