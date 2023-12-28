starting = int(input("Enter starting intervel to print all prime numbers = "))
ending = int(input("Enter ending intervel  = "))
def prime(num1,num2):
    for num in range(num1,num2,1):
        if num>1:
            for i in range(2,num):
                if num%i == 0:
                    break
            else:
                print(num)
            
prime(starting,ending)
