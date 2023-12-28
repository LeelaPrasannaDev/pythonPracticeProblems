num = int(input("Enter a number to print table = "))
# for loop
'''
def table(a):
    for i in range(1,11,1):
        print("{} * {} = ".format(a,i),(num*i))
    
table(num)

'''

# using while loop

def table(a):
    i=1
    while(i<= 10):
        print("{} * {} = ".format(a,i),(num*i))
        i=i+1

table(num)