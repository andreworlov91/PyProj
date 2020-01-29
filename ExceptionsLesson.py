import sys

filename = "my_passwords.txt"

while True:
    try:
        print("INSIDE TRY")
        myfile = open(filename, mode='r', encoding='Latin-1')
    except Exception:
        print("Inside EXCEPT")
        print("Error Found!")
        print(sys.exc_info()[1])
        filename = input("Enter correct file name! : ")
    else:
        print("Inside ELSE")
        print(myfile.read())
        sys.exit()