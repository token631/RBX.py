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
"""
In this segment, we simply loop through our list of name_id_data_type instances and print the friend/group name and the friend/group id.
"""
Friends = UserObj.GetUserFriends()
for Friend in Friends:
  print(f"{Friend.Name} | {Friend.Id}")

Groups = UserObj.GetUserGroups()
for Group in Groups:
  print(f"{Group.Name} | {Group.Id}")
  
# OR
"""
In this segment, we create two different lists for friend/group IDs and friend/group names. We loop through our table of name_id_data_type instances and then 
insert the friend/group ID and friend/group name into its respective list. This is much better for organization purposes.
"""
ListOfFriends_By_Name = []
ListOfFriends_By_ID = []

Friends = UserObj.GetUserFriends()
for Friend in Friends:
  ListOfFriends_By_ID.append(Friend.Id)
  ListOfFriends_By_Name.append(Friend.Name)

ListOfGroups_By_Name = []
ListOfGroups_By_ID = []

Groups = UserObj.GetUserGroups()
for Group in Groups:
  ListOfGroups_By_ID.append(Group.Id)
  ListOfGroups_By_Name.append(Group.Name)
  

# Other neat functions that do not return name_id_data_type instances
print(UserObj.GetUserIcon())
print(UserObj.GetFollowerCount())
