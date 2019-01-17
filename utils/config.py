"""
------------------------------
Ralsei utils/Config
Written by Infinidoge
------------------------------
Description:
    Utility base for managing Ralsei configs. Provides the Config class, which will be typically
    instantiated to provide configuration information to the Ralsei class
------------------------------
"""

# ------------------------------
#           Imports

# Config Parser - Allows creation, modification, and reading of .ini config files
from configparser import ConfigParser, ExtendedInterpolation

# Utils
from utils.misc import *

# ------------------------------


class Config:
    """
    Configuration Class
    ------------------------------
    Description:
        Stores and manages configuration information retrieved from a config file.
        If there is no config file, it will create a config file.
        If there is a config file, and it is of an older version, it will attempt to update the config file.
        Note:
            Automatic updating of the config file will only be supported to the latest major release version,
            and the latest developer release version.

            If the config file does not change from the previous version when an update is released,
            automatic migration will continue to work with previous versions.
    ------------------------------
    Parameters: (Arguments for when you instantiate the class.)

        config_file: Optional argument for what the config file name should be. (must end in .ini)
                     If not provided, defaults to RalseiConfig.ini
    ------------------------------
    Public Methods:

        config.refresh():
            Updates all values within the class to match the new values within the configuration.
            Please note, this will not refresh most options without a restart of Ralsei.
            (A restart command is provided in the base commands of Ralsei.)

        config.update({config_field}, {new_value}:
            Changes the value in config_field of the config file to become new_value.

        config.batch_update({set}):
            Takes a dictionary of field:value key pairs and updates all of them in order before updating the config
            Note: will only update attributes that are listed in the config file, all others will be ignored


    Internal Methods: (These should not be used outside of the class itself)
                      (Note, these methods use the config_file name that is provided when you instantiate the class,
                       you may manually provide a config file name to these methods if you decide to use them)

        config._read([config_file]):
            Reads the given config file (based on the name provided as the config_file parameter)
            This is used within refresh to set and update all of the values within the class to match the file
            Returns a configparser instance of config_file

        config._write([config_file]):
            Writes data to the config file based on the current stored values within the class.
            Primarily used to change config file values using config.update()

        config._create([config_file]):
            Creates a configuration file for Ralsei and fills in all relevant categories with default values.

    """

    def _read(self, config_file=None):
        """
        Reads config_file and returns a configparser object of it

        :param config_file:
        :return config:
        """
        config_file = config_file if config_file is not None else self.config_file

        config = ConfigParser(interpolation=ExtendedInterpolation())
        config.read(config_file)

        if not config.sections():
            self._create()

        return config

    def _write(self, config_file=None):
        """
        Updates config_file with all of the current attribute values

        :param config_file:
        :return:
        """

        config_file = config_file if config_file is not None else self.config_file

        config = ConfigParser(interpolation=ExtendedInterpolation())
        config.read(config_file)

        for i in config.sections():
            for x in config[i]:
                config[i][x] = self.__getattribute__(x)

        with open(config_file, 'w') as configfile:
            config.write(configfile)

    def _create(self, config_file=None):
        """
        Creates config_file and fills in the default attributes

        :param config_file:
        :return:
        """

        config_file = config_file if config_file is not None else self.config_file

        config = ConfigParser(interpolation=ExtendedInterpolation())

        config["RalseiBase"] = {"token":  "",
                                "app_id": ""}

        config["RalseiConfig"] = {"owner_id": "",
                                  "command_prefix": "!",
                                  "case_insensitive": "False",
                                  "pm_help": "False"}

        config["RalseiPaths"] = {"Ralsei_Dir": "",
                                 "CMDs_Dir": "%{Ralsei_Dir}/cmds",
                                 "Cogs_Dir": "%{Ralsei_Dir}/cogs"}

        config["RalseiPresence"] = {"RalseiPlaying": "In an Unknown World",
                                    "HostDetails":   "In an Unknown World",
                                    "HostState":     "Most likely with python",
                                    "HostLargeImg":  "ralsei_uh",
                                    "HostLargeTxt":  "Nothing to see here",
                                    "HostSmallImg":  "",
                                    "HostSmallTxt":  ""}

        with open(config_file, 'w') as configfile:
            config.write(configfile)

        self.refresh()

    def __init__(self, config_file="RalseiConfig.ini"):
        """
        Sets up the config class by reading config_file

        :param config_file:
        """

        self.config_file = config_file
        self.refresh()

    def refresh(self):
        """
        Refreshes the values of the instance to match the current version of the config file.

        :return:
        """
        config = self._read()
        for i in config.sections():
            for x in config[i]:
                self.__setattr__(x, config[i][x])

    def update(self, field, value):
        """
        Updates field within the config file to match value

        :param field:
        :param value:
        :return:
        """
        self.__setattr__(field, value)
        self._write()

    def batch_update(self, set: dict):
        """
        Takes a dictionary of field:value key pairs and updates all of them in order before updating the config
        Note: will only update attributes that are listed in the config file, all others will be ignored

        :param set:
        :return:
        """
        for i in set.keys():
            if i in get_vars(self):
                self.__setattr__(i, set[i])

        self._write()
