num = int(input("Enter a three digit number to check it is armstrong or not = "))

def arm(a):
    sum =0 
    temp = a
    order = len(str(a))
    while temp>0:
        digit = temp%10
        cube = digit**order
        sum = sum+cube
        temp = temp//10

    if sum == a:
        print("It is an armstrong numbner")
    else:
        print("It is not a armstrong number")

arm(num)