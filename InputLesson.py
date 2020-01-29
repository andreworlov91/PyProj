# name = input("Please enter Your name: ")
#
# print('Privet ' + name)
#
# num1 = input("Enter X: ")
# num2 = input("Enter Y: ")
#
# summa = int(num1) + int(num2)
# print(summa)
message = ""
while message != 'secret':
    message = input("Enter password ")
    if message == 'secret':
      break
    print(message + " Password Is Not Correct")

# myList = []
# msg = ""
# while msg != 'stop'.upper():
#     msg = input("Enter new item and STOP to finish: ")
#     myList.append(msg)
#
# print(myList)
# del myList[-1]
# print(myList)
# myList.pop()
# print(myList)