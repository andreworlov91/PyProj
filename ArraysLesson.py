# ---------------------------------------
# Program by Orlov.A.
#
#
# Version     Date      Info
# 1.0         2016   Initial Version
#
# ----------------------------------------

cities = ['New York', 'Moscow', 'new dehli', 'Simferopol', 'Toronto']
print(cities)
print(len(cities))
print(cities[-2])
print(cities[2].title())
cities[2] = 'Tula'
print(cities)
cities.append('Pskov')
print(cities)
cities.insert(0, 'Los Santos')
print(cities)
del cities[-1]
print(cities)
cities.remove('Tula')
print(cities)

deleted_city = cities.pop()
print("deleted city is: " + deleted_city)

cities.sort()
print(cities)

cities.sort(reverse = True)
print(cities)

cities.reverse()
print(cities)