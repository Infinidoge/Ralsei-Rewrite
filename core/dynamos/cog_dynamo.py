"""
Ralsei Core | Dynamos | Cog Dynamo
------------------------------
Description:
    The Cog Dynamo is the Ralsei Dynamo (or 'engine') for managing cogs themselves.
    This pertains to adding events through the Event Dynamo, and adding the cog normally.
    For registering commands to a cog without a cog file, the Command Dynamo will employ the Cog Dynamo

    Within this file is also the base cog class, of which all cogs will inherit.
    This base cog class defines how a cog registers events, etc.
"""


class Cog:
    """
    The base class of a cog for Ralsei
    """
    EventDynamo = None
    bot = None

    @classmethod
    def _init(cls, bot):
        cls.EventDynamo = bot.dynamos["Events"]
        cls.bot = bot
