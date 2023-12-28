# prime = number which is div by 1 and itself

num = int(input("Enter a number to check it is prime number or not = "))

def prime(a):
    flag = False
    if a==1:
        print("1 is not a prime number...")
    if a>1:
        for i in range(2,a,1):
            if a%i ==0:
                flag = True
                return flag
        else:
            return flag


result = prime(num)

if result is True:
    print("{} is not a prime number.....".format(num))
else:
    print("{} is a prime number......".format(num))