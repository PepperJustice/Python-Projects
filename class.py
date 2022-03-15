# class inheritance assignment
# Author Carla Justice


# creating parent class-client
class Client:
    name = 'No Name Provided'
    email = ' '
    account_number = 0

# child class VIP client with 2 specific attributes
class VIP(Client):
    bonus_package = 'Elite'
    status = 'Priority'

#child class Collab from client with 2 attributes
class Collab(Client):
    title = 'Collaborator'
    department = 'General'
