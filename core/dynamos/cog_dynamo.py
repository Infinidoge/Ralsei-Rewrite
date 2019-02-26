"""
Ralsei Core | Dynamos | Cog Dynamo
------------------------------
Description:
    The Cog Dynamo is the Ralsei Dynamo (or 'engine') for managing cogs themselves.
    For registering commands to a cog without a cog file, the Command Dynamo will employ the Cog Dynamo
"""

from utils.misc import get_files, get_func, get_vars


class CogDynamo:
    def __init__(self, bot, additional_cogs=[]):
        self.bot = bot
        self.cogs = additional_cogs

    def _get_cogs(self, cog_dir):
        for cls in [i.__getattribute__(get_func(i)[0]) for i in
                    (lambda z: [z.__getattribute__(x) for x in get_vars(z)])(
                        __import__("cogs", fromlist=[i[:len(i) - 3] for i in
                                                     get_files(cog_dir)]))]:
            self._add_cog(cls(self.bot))

    def _add_cog(self, cog):
        self.cogs += [cog]

    def _load_cogs(self):
        _last = None
        print("---------------------------------------")
        print("|             Cogs Loaded             |")
        print("---------------------------------------")
        for cog in self.cogs:
            try:
                _last = True
                print(f"| {type(cog).__name__}{' '*(36-len(type(cog).__name__))}|")
                self.bot.add_cog(cog)
            except Exception as e:
                _last = False
                print("---------------------------------------")
                print(f"Cog Failed: {type(cog).__name__}\nException:\n{e}")
                print("---------------------------------------")
        if _last:
            print("---------------------------------------")

    def init_cogs(self):
        self._get_cogs(self.bot.config.cogs_dir)
        self._load_cogs()
