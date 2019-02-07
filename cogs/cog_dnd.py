"""
------------------------------
Ralsei cogs/dnd
Written by Infinidoge
------------------------------
Description:
    Cog for Ralsei containing all commands related to running D&D
------------------------------
Contributors:
    - Infinidoge (Creator)
------------------------------
Misc Notes:
  - None -
"""

# ------------------------------
#            Imports

# Random - generates random results
import random

# Asyncio - utilities for asynchronous programming
import asyncio

# Discord - provides an interface with discord to create a bot and allow it to function
from discord.ext import commands

# misc - Misc utils
from utils.misc import *

# ------------------------------


class DnD:
    """
    Ralsei cogs/DnD
    ------------------------------
    Description:
        Cog for Ralsei containing all commands related to running D&D
    ------------------------------
    Events:
      - Not Applicable -
    ------------------------------
    Classes:
      - StatBlock
            Represents a stat block, either a base stat block (just 6 numbers) or a stat block for a creature
            (6 stats assigned to strength [str], dexterity [dex], constitution [con],
            intelligence [int], wisdom [wis], and charisma [cha].)
    """

    class StatBlock:
        """
        Ralsei cogs/DnD/StatBlock
        ------------------------------
        Description:
            Represents a stat block for any given D&D object, whether it is a character or monter, the core stats
            are the of the same types
        ------------------------------
        """

        class StatGeneration:
            """
            Ralsei cogs/DnD/StatBlock/StatGeneration
            ------------------------------
            Description:
                Nested class within StatBlock to house internal stat generation methods
            ------------------------------
            """

            @staticmethod
            def d20_standard():
                """"""
                stat_block = []
                while sum(stat_block) < 70:
                    stat_block = []
                    for i in range(6):
                        num = 0

                        while num < 6:
                            num = random.randint(1, 20)
                        stat_block.append(num)
                stat_block.sort()
                num = 0
                while num < 6:
                    num = random.randint(1, 20)

                replace_greater(stat_block, 0, num)

                stat_block.sort()
                return stat_block

        def __str__(self):
            if not self.raw:
                return "[{str}] | [{dex}] | [{con}] | [{int}] | [{wis}] | [{cha}]".format()
            else:
                return "{} | {} | {} | {} | {} | {}".format(self.raw_block[0], self.raw_block[1],
                                                            self.raw_block[2], self.raw_block[3],
                                                            self.raw_block[4], self.raw_block[5])

        # def __getattr__(self, item):
        #     pass

        # def __setattr__(self, key, value):
        #     pass

        def __init__(self, generation_method=None):
            self.raw = True

            if self.raw:
                self.raw_block = self.StatGeneration.d20_standard()

            else:
                self.block = (lambda keys, values:
                             {keys[i]: values[i] for i in range(len(keys))})(
                    ["str", "dex", "con", "int", "wis", "cha"], self.StatGeneration.d20_standard())

        def _get(self):
            print(self.raw_block)
            print(self.block)

    def __init__(self, ralsei):
        self.ralsei = ralsei
        type(self).__name__ = 'D&D'

    @commands.command()
    async def genstats(self, ctx):
        await ctx.send(str(self.StatBlock()))
