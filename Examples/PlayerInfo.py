import RBX_py
from RBX_py import Client

# Initialise the Client
RBX_Client = Client()

# Create an Asset object via using the fetch function
UserObj = RBX_Client.FetchUser(327834301)

# Print some of its properties
print(UserObj.Name)
print(UserObj.Description)
print(UserObj.ProfileLink)
print(UserObj.CreatedAt)

# Work with the object's functions

# The GetUserFriends and GetUserGroups functions will return a list of name_id_data_type instances. This, as the name suggests, provides an object that stores the supplied name and id 

Friends = UserObj.GetUserFriends()
for Friend in Friends:
  print(f"{Friend.Name} | {Friend.Id}")

Groups = UserObj.GetUserGroups()
for Group in Groups:
  print(f"{Group.Name} | {Group.Id}")

print(UserObj.GetUserIcon())
print(UserObj.GetFollowerCount())
