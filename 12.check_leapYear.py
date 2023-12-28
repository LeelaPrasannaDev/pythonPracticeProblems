# year with 400 and 100 equal to zero then leap year for century years 
# for non century years year with 4 equal to zero and year with 100 not equal to zero then also leap year



year = int(input("Enter a year to check leap year or not = "))
def leap(a):
    flag = False
    if (a % 400 == 0) and (a % 100 == 0):
        flag = True
        return flag
    elif (a % 4 == 0) and (a % 100 != 0):
        flag = True
        return flag
    else:
        return flag
    
check = leap(year)

if check is True:
    print("{} is a leap year..".format(year))
else:
    print("{} is not a leap year".format(year))


'''
year = 2000

if (year % 400 ==0 ) and (year % 100 == 0):
    print("leap year")
elif (year % 4 ==0) and (year % 100 !=0):
    print ("leap year")
else:
    print("not")
'''
