num = int(input("Enter a number to find factorial = "))

def fact(a):
    if a<0:
        print("Factorial of zero does not exist")
    if a==0:
        print("Factorial of 0 is 1")
    if a>0:
        result =1
        for i in range(1,a+1,1):
            result = result*i
    print("The factorial of given number is = ",result)

fact(num)