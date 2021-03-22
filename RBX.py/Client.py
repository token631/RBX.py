"""
RBX.py/Client.py

The heart of the RBX.py library;
This class is what actually fetches the different object instances and is essentially the bridge between the user and the rest of the library.
"""

from RBX_py.Asset import Asset
from RBX_py.Player import Player

class Client:
    def __init__(self):
        pass

    def FetchAsset(self, id):
        """
        Creates an instance of an Asset class using the given ID
        """
        TypeErrorCheck = isinstance(id, str)
        if TypeErrorCheck:
            raise TypeError(f"Asset ID ({Asset_id}) must be in integer form")

        asset_obj = Asset(id=id)
        asset_obj.fetchData()
        return asset_obj
    
    def FetchUser(self, id):
        """
        Creates an instance of a Player class using the given ID
        """
        TypeErrorCheck = isinstance(id, str)
        if TypeErrorCheck:
            raise TypeError(f"User ID ({id}) must be in integer form")

        player_obj = Player(id=id)
        player_obj.fetchData()
        return player_obj
