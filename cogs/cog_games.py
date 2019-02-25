"""
------------------------------
Ralsei cogs/games
Written by Infinidoge
------------------------------
Description:
    Cog for Ralsei containing simple games, such as Rock, Paper, Scissors
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

# ------------------------------


class Games(commands.Cog):
    """
    Ralsei cogs/games
    ------------------------------
    Description:
        Cog for Ralsei containing simple games, such as Rock, Paper, Scissors.
        Eventually more complex games may be added. Multiple games of the same category, such as card games,
        may get their own sub-cog, imported by the main games cog. (However, they will be shown as a separate
        cog when viewed in the help command)
    ------------------------------
    Events:
      - Not Applicable -
    ------------------------------
    Classes:
      - Not Applicable -
    """

    @commands.command()
    async def rps(self, ctx, *, player_move=None):
        """
        Play a game of Rock, Paper, Scissors with Ralsei!

        :param ctx:
        :param player_move: Move the player selects
        :return:
        """
        com_move = random.randint(1, 3)
        if player_move is None:
            await ctx.send("I choose roc- oh, \n"
                           "can you try running the command with a move of either Rock, Paper, or Scissors? \n"
                           "(and they can be lowercase)")
        elif player_move.lower() not in ["rock", "paper", "scissors"]:
            await ctx.send("That isn't rock, paper, or scissors. Try again?")
        else:
            player_move = 1 if (player_move.lower() == "rock") else 2 if (player_move.lower() == "paper") else 3

            game = await ctx.send("Let's Play!")
            await asyncio.sleep(1)
            await game.edit(content="Rock,")
            await asyncio.sleep(0.5)
            await game.edit(content="Rock, \nPaper,")
            await asyncio.sleep(0.5)
            await game.edit(content="Rock, \nPaper, \nScissors!")
            await asyncio.sleep(1)
            await ctx.send(content="I choose %s!" % ("rock" if (com_move == 1) else
                                                      "paper" if (com_move == 2) else
                                                      "scissors"))
            await asyncio.sleep(0.5)
            await ctx.send("Sorry, I win!" if (com_move > player_move or com_move == 3 and player_move == 1) else
                           "Congrats, you win!" if (player_move > com_move or player_move == 3 and com_move == 1) else
                           "Ah well, it's a tie!")
