"""
Ralsei Core | Dynamos | Extensions Dynamo
------------------------------
Description:
    The Extend Dynamo is the Ralsei Dynamo (or 'engine') for managing extensions.
    Extensions are pieces of code that can be added or removed from the bot while the bot is running.
"""

from discord.ext import commands
from discord import ClientException
import discord


class ExtendDynamo:
    class ExtensionManagement(commands.Cog, name="Extension Management", command_attrs=dict(hidden=True)):
        def __init__(self, bot, dynamo):
            self.bot = bot
            self.dynamo = dynamo

        @commands.group(name="ext", invoke_without_command=True)
        async def extension(self, ctx):
            newline = "\n"
            await ctx.send(embed=discord.Embed(
                title="Loaded Extensions" if len(self.dynamo.extensions) > 0 else
                      "`No Extensions Loaded`",
                description=f"{newline.join([f'`{i}`' for i in self.dynamo.extensions])}" if
                            0 < len(self.dynamo.extensions) else ""))

        @extension.command(aliases=["+"])
        async def add(self, ctx, extension: str):
            await ctx.send(self.dynamo.load_extension(extension))

        @extension.command(aliases=["del", "-"])
        async def remove(self, ctx, extension: str):
            await ctx.send(self.dynamo.unload_extension(extension))

        @extension.command(aliases=["rel", "|"])
        async def reload(self, ctx, extension: str):
            await ctx.send(self.dynamo.reload_extension(extension))

        @extension.command(aliases=["rel_all", "||"])
        async def reload_all(self, ctx):
            await ctx.send(self.dynamo.reload_all())

    def __init__(self, bot):
        self.bot = bot
        self.extensions = []

    def load_extension(self, extension: str):
        try:
            self.bot.load_extension(extension)
            self.extensions.append(extension)

            print(f"""
----------------------------------------
| Extension {extension}{' '*(16-len(extension))} Loaded    |
----------------------------------------""")

            return f"`Extension {extension} loaded successfully`"
        except ImportError:
            print(f"""
----------------------------------------
| Extension {extension}{' '*(16-len(extension))} Failed    |
----------------------------------------
| Error: Extension failed to import    |
----------------------------------------""")

            return f"`Error: Extension {extension} could not be imported`"
        except ClientException:
            print(f"""
----------------------------------------
| Extension {extension}{' '*(16-len(extension))} Failed    |
----------------------------------------
| Error: Extension lacks setup func    |
----------------------------------------""")

            return f"`Error: Extension {extension} does not have a setup function`"

    def unload_extension(self, extension: str):
        if extension in self.extensions:
            self.bot.unload_extension(extension)
            self.extensions.remove(extension)
            return f"`Extension {extension} unloaded`"
        else:
            return f"`Extension {extension} not loaded.`"

    def reload_extension(self, extension: str):
        if extension in self.extensions:
            self.bot.unload_extension(extension)
            self.bot.load_extension(extension)
            return f"`Extension {extension} reloaded`"
        else:
            return f"`Extension {extension} not loaded.`"

    def reload_all(self):
        for extension in self.extensions:
            self.reload_extension(extension)

        return f"`All extensions reloaded`"

    def __call__(self):
        return self.ExtensionManagement(self.bot, self)

