#f = (c*9/5)+32

c = float(input("Enter temparature in celsius = "))

def fah(celsius):
    fahrenheit = (celsius*9/5)+32
    return fahrenheit

temp = fah(c)
print("{} degrees celsius is equal to {} in fahrengeit".format(c,temp))