"""
------------------------------
Ralsei utils/Misc
------------------------------
Description:
    Utility file containing random functions, etc that are used elsewhere.
------------------------------
"""

# ------------------------------
#           Imports

# os - operating system level utilities
from os import listdir
from os.path import isfile, join

# ------------------------------


def get_vars(cls):
    """
    Takes an input class (cls) and returns all attributes of the class,
    not including functions or __ special attributes/functions

    :param cls:
    :return variables:
    """

    return [a for a in dir(cls) if not a.startswith('__') and not callable(getattr(cls,a))]


def get_func(cls):
    """
    Takes an input class (cls) and returns all callable attributes of the class,
    not including __ special attributes/callable attributes

    :param cls:
    :return functions:
    """

    return [a for a in dir(cls) if not a.startswith('__') and callable(getattr(cls, a))]


def get_all(cls):
    """
    Takes an input class (cls) and returns all attributes,
    including functions and __ special attributes/functions

    :param cls:
    :return attributes:
    """

    return [a for a in dir(cls)]


def get_files(path):
    """
    Takes an input path to a directory and returns a list of the filenames of all of the files in said directory


    :param path:
    :return files:
    """

    return [f for f in listdir(path) if isfile(join(path, f))]


def replace_greater(iterable, index, val):
    """
    Takes an iterable, iter, and replaces the value at index with val if val is greater than the value at index

    :param iterable:
    :param index:
    :param val:
    :return:
    """
    iterable[index] = val if iterable[index] < val else iterable[index]
    return iterable


def replace_lesser(iterable, index, val):
    """
    Takes an iterable (iterable) and replaces the value at index with val if val is less than than the value at index

    :param iterable:
    :param index:
    :param val:
    :return:
    """
    iterable[index] = val if iterable[index] < val else iterable[index]
    return iterable
