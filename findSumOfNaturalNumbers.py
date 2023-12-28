# natural numbers = all positive numbers from 0 to infinitie 

num = int(input("Enter a numberto find the sum of natural numbers upto this number = "))

def natural(num):
    if num<0:
        message = 'below zero are not natural numbers'
        return message
    else:
        sum = 0
        while num>0:
            sum = sum+num
            num = num-1

    return sum

result = natural(num)
print(result)