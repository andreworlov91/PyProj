# ---------------------------------------
# Program by Orlov.A.
#
#
# Version     Date      Info
# 1.0         2016   Initial Version
#
# ----------------------------------------

# x = 25
#
# if x == 25:
#     print("YES, yo're right")
# else:
#     print("NO!!!!!!!!!!!!!!!!!!!!!!!!")
age = 13
if (age <= 4):
    print("you are baby!")
elif (age > 4) and (age <= 12):
    print("you're kid!")
else:
    print("you will die soon :3")

print("-------------END-----------")

cars = ['bmw', 'vw', 'seat', 'skoda', 'lada']
german_cars = ['bmw', 'vw', 'audi']
# if 'lada' in cars:
#     print('omg... lada')
# else:
#     print('mb will you buy some car?')

for xxx in cars:
    if xxx in german_cars:
        print(xxx + " is german car")
    else:
        print(xxx + " is not german car")