# 1km = 0.621371 mile

km = float(input("Enter Kilometers to convert into miles = "))

def miles(a):
    mil = a*0.621371
    return mil

Kt0M=miles(km)
print("{} kilometers equals to {} in miles,".format(km,Kt0M))