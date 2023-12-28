num = float(input("Enter a number to check even od odd = "))

def check(a):
    if a%2==0:
        return True
    else:
        return False
    
even_or_odd = check(num)
if even_or_odd is True:
    print("{} is an even number..".format(num))
else:
    print("{} is an odd number....".format(num))