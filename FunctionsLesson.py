# def - функция
def write_hello(name):
    """"Print privet"""
    print("Congratulations, wish you all the best " + name)
    print("Hello HELLOOOOOOOOOOOOOOO HELLLLLLOOOO!!! " + name)


def a(x, y):
    return x + y


def factorial(x):
    octet = 1
    for i in range(1, x + 1):
        octet = octet * i
    return octet


# -----------------------------------------

print("--------------------------------------")

write_hello("ANDREY")
b = a(23, 7)
print(b)
print(factorial(-1))