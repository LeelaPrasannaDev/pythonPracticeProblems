# Quadratic equation = (-b+sqr((b**2)-4ac))/2a

a = float(input('Enter a value where (a!=0) = '))
b= float(input('Enter b value = '))
c = float(input('Enter c value  = '))

if a==0:
    print("please enter A value grater than zero.......")
else:
    def equation(a,b,c):
        sqr = ((b**2)-4*a*c)**(0.5)
        Quadratic1 = (-b-sqr)/2*a
        Quadratic2 = (-b+sqr)/2*a
        return Quadratic1,Quadratic2
    
    print(equation(a,b,c))