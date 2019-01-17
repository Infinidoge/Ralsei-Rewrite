"""
------------------------------
Ralsei utils/Misc
------------------------------
Description:
    Utility file containing random functions, etc that are used elsewhere.
------------------------------
"""


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
