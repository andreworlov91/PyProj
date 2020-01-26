# ---------------------------------------
# Program by Orlov.A.
#
#
# Version     Date      Info
# 1.0         2016   Initial Version
#
# ----------------------------------------

cars = ['bmw', 'vw', 'seat', 'skoda', 'lada']

for x in cars:
    print(x.upper())

for x in range(1, 6):
    print(x)

myNumberList = list(range(0, 10))
print(myNumberList)
newList = list
print(len(list([1])))

print("Max number is: " + str(max(myNumberList)))
print("Min number is: " + str(min(myNumberList)))
print("Sum of numbers is: " + str(sum(myNumberList)))

mycars = cars[1:4] # от первого до третьего. первый включает. четвертый нет
print(mycars)
print(cars[:4])

mycars = cars # такая же история как со ссылками на один объект в Java
print(mycars)

cars.pop()
print(cars)
print(mycars)