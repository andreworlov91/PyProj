# ---------------------------------------
# Program by Orlov.A.
#
#
# Version     Date      Info
# 1.0         2016   Initial Version
#
# ----------------------------------------

for x in range(0, 100, 2):
    print("Number " + str(x))
    if x == 50:
        break
print("--------------EOF--------------")

x = 0

while True:
    print(x)
    x = x + 1
    if x == 100:
        break