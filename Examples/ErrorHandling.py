import RBX_py
from RBX_py import Client

# Initialise the Client
RBX_Client = Client()

# Let's make a function that will return a user obj based on user input
def fetchUser(userid : int):
  try:                               
    UserObj = RBX_Client.FetchUser(userid)  #Try to fetch a user object with the given ID
    return UserObj
  except RBX_py.PlayerNotFound: # Catch the PlayerNotFound exception!
    return("User cannot be found") # Put a neat lil' error message here

print(fetchUser(0)) # This will print "User cannot be found"
print(fetchUser(1)) # This will return a user object

"""
This file uses the PlayerNotFound exception as an example, however please note that this can be applied to virtually anything.
Every RBX.py exception can be located in RBX.py / RBX.py / Errors.py 
"""
