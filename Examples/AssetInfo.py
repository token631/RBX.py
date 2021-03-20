import RBX_py
from RBX_py import Client

# Initialise the Client
RBX_Client = Client()

# Create an Asset object via using the fetch function
AssetObj = RBX_Client.FetchAsset(456225312)

# Print some of its properties
print(AssetObj.Name)
print(AssetObj.Price)
print(AssetObj.Creator)
