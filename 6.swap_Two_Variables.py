# swap two variables by using 3rd variable

'''

var1 = int(input("Enter 1st number to swap = "))
var2 = int(input("Enter 2st number to swap = "))
print("before swap 1st value = ",var1)
print("before swap 1st value = ",var2)


def swap(a,b):
    temp = a
    a = b
    b = temp
    return a,b

print("After swap...")
values = list(swap(var1,var2))
print("After swap 1st value = ",values[0])
print("After swap 2st value = ",values[1])

'''

# swap two values without using 3rd variable

var1= int(input("Enter 1st number to swap = "))
var2=int(input("Enter 2st number to swap = "))
print("before swap 1st value = ",var1)
print("before swap 1st value = ",var2)
print("After swap...")
var1,var2 = var2,var1
print("After swap 1st value = ",var1)
print("After swap 2st value = ",var2)
