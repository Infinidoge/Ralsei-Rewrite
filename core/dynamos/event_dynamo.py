"""
Ralsei Core | Dynamos | Event Dynamo
------------------------------
Description:
    The event dynamo is the Ralsei Dynamo (or 'engine') for managing events defined within cogs
    To handle events, Ralsei will have every Discord event defined in the main class, then the event dynamo will
    handle functionality for each event. Instead of a static event registration, Ralsei will run the event and the
    event dynamo will go through all of the cogs adding functionality to the event, running each bit of functionality
    in order of priority (defined in the event definition within the cog.)
"""

# ------------------------------
#            Imports

# Discord - provides an interface with discord to create a bot and allow it to function
import discord
import discord.ext.commands as commands

# Asyncio - utilities and pieces for asynchronous programming
import asyncio

# inspect - allows for inspecting things (such as getting the name of the current function or its caller
import inspect

# Utils
from utils.misc import *

# ------------------------------


class EventDynamo:
    """
    Ralsei Core | Dynamos | Event Dynamo | Event Dynamo Class
    ------------------------------
    Description:
        The class representing the Event Dynamo itself.
    """

    class Events:
        """
        Ralsei Core | Dynamos | Event Dynamo | Event Dynamo Class | Events
        ------------------------------
        Description:
            Class containing all of the Discord.py events available to the bot.
            This will also contain a subclass containing default event functionality, which won't be removed.
        ------------------------------
        Notes:
          - This depreciates the Ralsei Base Events class as soon as it is implemented.
        """

        def __init__(self, bot, event_def: dict, async_event_def: dict):
            self.async_events = async_event_def
            self.events = event_def
            self.bot = bot

        def collect_events(self):
            return [self.__getattribute__(i) for i in get_startswith(self, "on_")]

        def event(self, event, *args, **kwargs):
            print("Logs: Event : |"+event+"|")

            for func in self.events[event]:
                func(*args, **kwargs)

        async def async_event(self, event, *args, **kwargs):
            print("Logs: Async Event: |"+event+"|")
            try:
                for func in self.async_events[event]:
                    await func(*args, **kwargs)
            except KeyError:
                pass

        async def on_connect(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_ready(self, *args, **kwargs):
            print("Ralsei  |  Online")
            print("-------------------------")
            print("| Logged in as:         |")
            print("|  %s               |" % self.bot.user.name)
            print("|-----------------------|")
            print("| Id: %s|" % self.bot.user.id)
            print("-------------------------")
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_resumed(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_error(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_socket_raw_receive(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_socket_raw_send(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_typing(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_message_delete(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_raw_message_delete(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_raw_bulk_message_delete(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_message_edit(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_message(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_raw_message_edit(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_reaction_add(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_raw_reaction_add(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_reaction_remove(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_raw_reaction_remove(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_reaction_clear(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_raw_reaction_clear(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_private_channel_create(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_private_channel_delete(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_private_channel_update(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_private_channel_pins_update(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_guild_channel_create(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_guild_channel_delete(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_guild_channel_update(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_guild_channel_pins_update(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_webhooks_update(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_member_join(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_member_remove(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_member_update(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_guild_join(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_guild_remove(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_guild_update(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_guild_role_create(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_guild_role_delete(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_guild_role_update(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_guild_emojis_update(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_guild_available(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_guild_unavailable(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_voice_state_update(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_member_ban(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_member_unban(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_group_join(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_group_remove(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_relationship_add(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_relationship_remove(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

        async def on_relationship_update(self, *args, **kwargs):
            await self.async_event(inspect.currentframe().f_code.co_name, *args, **kwargs)

    def __init__(self, bot, event_def: dict, async_event_def: dict):
        self.bot = bot
        self.event_def = event_def
        self.async_event_def = async_event_def

        self.events = self.Events(bot, event_def, async_event_def)

        for i in self.events.collect_events():
            self.bot.event(i)

    def event(self):
        pass

    def async_event(self):
        pass

    # TODO: Function that extracts event definitions from a class

    def add_event(self, event: str, func: callable):
        self.event_def[event].append(func)

    def add_async_event(self, event: str, func: callable):
        self.async_event_def[event].append(func)