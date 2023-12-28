num = int(input("Enter a number to print fibonacci sequence upto given number = "))

def febi(a):
    b = 0
    c = 1
    if a ==1:
        print(b)
    else:
        print(b)
        print(c)
        for i in range (1,a,1):
            d = b+c
            b = c
            c = d
            print(d)

febi(num)

