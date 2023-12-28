# lambda fuction 
# if user give 5 then 2**0, 2**1, 2**2, 2**3, 2**4, 2**5

nterms = int(input("Enter a term here = "))
# map = to modify the elements by performing operations on it
def power2(a):
    result = list(map(lambda x : 2**x, range(a+1)))
    return result

re = power2(nterms)
for i in range(1,nterms+1):
    print(" The value of 2 power {} is {}".format(i,re[i]))