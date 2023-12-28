num1 = float(input("Enter 1st number = "))
num2 = float(input("Enter 2nd number = "))
num3 = float(input("Enter 3rd number = "))

def greater(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
    
g = greater(num1,num2,num3)
print("{} is greater number among three...".format(g))