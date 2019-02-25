"""
Ralsei Core | Dynamos | Cog Dynamo
------------------------------
Description:
    The Cog Dynamo is the Ralsei Dynamo (or 'engine') for managing cogs themselves.
    For registering commands to a cog without a cog file, the Command Dynamo will employ the Cog Dynamo
"""


class CogDynamo:
    def __init__(self, bot):
        self.bot = bot
        self.cogs = []

    def add_cog(self, cog):
        print(f"Cog Loaded: {type(cog).__name__}")
        self.cogs += [cog]

    def load_cogs(self):
        for cog in self.cogs:
            self.bot.add_cog(cog)
