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
    - cog_dnd.py (Created by Infinidoge)
    - cog_games.py (Created by Infinidoge)

List of officially supported utils and their creators:
    - config.py (Created by Infinidoge)
    - misc.py (Various)

List of officially supported dynamos and their creators:
    - cog_dynamo (Created by Infinidoge)
------------------------------
Contributors:
    - Infinidoge (Creator)
------------------------------
Misc Notes:
  1.If you majorly fix or create a feature, such as a cog, and the pull request was accepted,
    let Infinidoge on GitHub know, and your name will be added to the contributors list.

  2.Doc strings for commands are formatted where anything within {} is a required argument,
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
from core.dynamos.cog_dynamo import *
import core.dynamos.extend_dynamo

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

    class BaseCommands(commands.Cog, name="Base Commands"):
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
            raise RalseiExit
            # Exits the loop without unclosed session errors as it mimics a keyboard interrupt
            # the exception is caught outside the loop

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

    async def on_ready(self):
        print(f"---------------------------------------")
        print(f"|   {self.name}{' '*(19-len(self.name))}  |   Online   |")
        print(f"---------------------------------------")
        print(f"| Logged in as:                       |")
        print(f"|  {self.user.name}{' '*(33-len(self.user.name))}  |")
        print(f"---------------------------------------")
        print(f"| ID: {self.user.id}{' '*(31-len(str(self.user.id)))} |")
        print(f"---------------------------------------")

    @staticmethod
    def _dynamic_prefix(bot, msg):
        return bot.config.command_prefix

    def __init__(self, config=Config()):
        self.config = config
        self.name = "Ralsei"

        self.dynamos = {"Cogs": CogDynamo(self, [
            self.BaseCommands(self)
        ]),
                        "Commands": "placeholder"}

        super(Ralsei, self).__init__(command_prefix=self._dynamic_prefix,
                                     activity=discord.Game(f"Somewhere, with "
                                                           f"`{self._dynamic_prefix(self, 'blank')}` as my prefix."))

        self.dynamos["Cogs"].init_cogs()

    def ralsei_run(self, token=None):
        try:
            try:
                self.run(token if token is not None else
                         self.config.token if self.config.token is not None and self.config.token is not ""
                         else input("Temp Token:"))
            except Exception as e:
                print("An Exception occurred when trying to run Ralsei with that token:\n%s" % str(e))
        except KeyboardInterrupt or RalseiExit:
            print(f"---------------------------------------")
            print(f"|   {self.name}{' ' * (18 - len(self.name))}  |   Offline   |")
            print(f"---------------------------------------")


ralsei = Ralsei()
ralsei.ralsei_run()
