t = input("Amalni kiriting: ")
a = int(input("1-sonni kiriting: "))
b = int(input("2-sonni kiriting: "))

def kopaytirish(a,b):
    if t == "*":
        print("a * b = " , a*b)
    elif t == "/":
        print("a / b = ", a/b)
    elif t == "+":
        print("a + b = ", a+b)    
    elif t == "-":
        print("a - b = ", a-b)
    else:
        print("Noto'g'ri amal kiritdingiz!")
kopaytirish(a, b)