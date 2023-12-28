startnum = int(input("Enter a starting number = "))
endnum = int(input("Enter a ending number = "))

def arm(a,b):
    for i in range(a,b+1):
        order = len(str(i))
        temp = i
        sum = 0 
        while temp > 0 :
            digit = temp %10
            power = digit**order
            sum = sum + power
            temp = temp//10
    
        if i == sum:
            print(i)

arm(startnum,endnum)