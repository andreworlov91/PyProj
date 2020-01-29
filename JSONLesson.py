import json

filename = "user_settings.json"
myfile = open(filename, mode='w', encoding='Latin-1')

player1 = {
    'PlayerName': "Donald Trump",
    'Score': 345,
    'awards': ["OR", "NV", "NY"]
}

player2 = {
    'PlayerName': "Clinton Hillary",
    'Score': 346,
    'awards': ["WT", "TX", "MI"]
}
myplayers = []
myplayers.append(player1)
myplayers.append(player2)


# -------------- SAVE by JSON ----------

json.dump(myplayers, myfile, indent=0)
myfile.close()

# ------------- LAOD by JSON -----------------

myfile = open(filename, mode='r', encoding='Latin-1')
json_data = json.load(myfile)

for user in json_data:
    print("Player Name is: " + str(user['PlayerName']))
    print("Player Score is: " + str(user['Score']))
    print("Player Award N1 is: " + str(user['awards'][0]))
    print("----------------------------------------\n\n")

myfile.close()