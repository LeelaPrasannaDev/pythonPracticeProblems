# Area of triangle = 1/2 * bredth * heoght

breadth = float(input("Enter breadth of the triangle = "))
height =  float(input("Enter height of the triangle = "))

def areaOfTriangle(a,b):
    area = (0.5*a*b)
    return area

area=areaOfTriangle(breadth,height)
print("Area of triangle = ",area)