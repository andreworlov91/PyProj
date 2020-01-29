
inputfile = "../rockyou.txt"
outputfile = "../my_passwords.txt"

password_tolookfor = "vasya"

myfile = open(inputfile, mode='r', encoding='latin1')
myfile2 = open(outputfile, mode='a', encoding='latin1')

for num, line in enumerate(myfile, 1): # в num загружается номер прочитанной строки
    if password_tolookfor in line:
        print("Line N: " + str(num) + " : " + line.strip())  # уберёт и пробелы и переносы строк
        myfile2.write("Found password: " + line)


myfile.close()
myfile2.close()