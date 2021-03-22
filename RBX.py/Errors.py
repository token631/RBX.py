"""
RBX.py/Errors.py

Simple exceptions that the lib throws
Please remember to catch these exceptions when possible!
"""

class Exc(Exception):
    pass

class AssetNotFound(Exc):
    """Thrown when asset cannot be located"""

class PlayerNotFound(Exc):
    """Thrown when player cannot be located"""
