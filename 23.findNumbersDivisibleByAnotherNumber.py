#if user give a range from 1 to 100 and also check number assume 13
# we need to check how many numbers in 1 to 100 is divisable by 13 and gives reminder 0 

'''
To slove this 

1. take user input of starting number in the range 
2. take another user input of ending number in the range 
3. and also take user input that which number we need to check if the range values is divisable by
4.by using for loop take values one by one in the range 
5. apply condition where the number is divisible by check number and gives reminder zero then it is divisible 
'''

# code start from here
# By using forloop and conditions
'''
start = int(input("Enter a starting number to start the range = "))
end = int(input("Enter end number to end the range = "))
target_number = int(input("Enter a number you need to check range is divisible by = "))
#starting a function where the logic return
def check_divisable(a,b,c):
   # taking empty list to store values
    values=[]
     # take forloop to acces all the numbers in the range
    for i in range(a,b):
        # condition to check divisible by check number
        if i%c==0:
            values.append(i)
        else:
            continue
    return values
#calling function
        
result = check_divisable(start,end,target_number)
print(" The numbers in range from {} to {}, which are divisible by {} are = {}".format(start,end,target_number,result))

'''

# By using lambda function and filter()
# filter = to filter elements based on condition

# create a list that need to check that numbers 

list_of_numbers = [1,2,3,4,5,6,7,8,9,10]
num = int(input("Enter a number to check = "))
result = list(filter(lambda x: x%num==0,list_of_numbers))
print("The numbers in the given list which are divisiable by given number = ",result)