num = float(input("Enter a number to check wheather its postive or negative = "))

def check(a):
    
    if a>0:
        print("{} is postive!".format(a))
    elif a==0:
        print("You entered zero, zero is not positive not negative..........")
    else:
        print("{} is negative!".format(a))

check(num)
    

    
