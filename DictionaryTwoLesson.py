import copy

enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'Mudillo',
    'image': ['image1.jpg', 'image2.jpg', 'image3.jpg']
}

allEnemies = []

for x in range(1, 10):
    allEnemies.append(copy.deepcopy(enemy))
    # allEnemies.append(enemy.copy())
print(len(allEnemies))
allEnemies[5]['health'] = 50
allEnemies[5]['image'][0] = 'suka'
for en in allEnemies:
    print(en)