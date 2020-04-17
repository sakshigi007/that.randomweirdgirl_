a=int(input("enter a number:\n"))
b=int(input("enter another number:\n"))


def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b


print("select operation:\n"
        "1. add\n"
        "2. subtract\n"
        "3. multiply\n"
        "4. divide\n")



select=input("enter a number(1/2/3/4)")
if select=='1':
    print(a, "+", b , "=", add(a,b))
elif select=='2':
    print(a, "-", b , "=", subtract(a,b))
elif select=='3':
    print(a, "*", b , "=", multiply(a,b))
elif select=='4':
    print(a, "/", b , "=", divide(a,b))
else:
    print("invalid")

