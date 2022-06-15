import json


filename = "c:/Users/admin/python/learn-py/json/players.txt"
my_file = open(filename,mode='w',encoding='utf-8')

player1 = {
    'Name' : 'Donald',
    'Score': 500,
    'Awards': ['NY','NJ','Texas']
}

player2 = {
    'Name' : 'Petya',
    'Score': 500,
    'Awards': ['NY','Florida','Texas']
}

my_players = []

my_players.append(player1)
my_players.append(player2)

#-----------Save by JSON-------------------------------------

json.dump(my_players,my_file)

my_file.close()

#-----------Load by JSON-------------------------------------

my_file = open(filename,mode='r',encoding='utf-8')

json_data = json.load(my_file)

for user in json_data:
    print("Player: " + str(user['Name']))
    print("Score: " + str(user['Score']))


print("=====================\n\n")