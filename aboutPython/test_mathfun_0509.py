import math
def quadratic_equation(a, b, c):
    x1=(-b+sqrt(b*b-4*a*c))/(2*a)
    x2=(-b-sqrt(b*b-4*a*c))/(2*a)
    return x1,x2
print (quadratic_equation(2, 3, 0))
print (quadratic_equation(1, -6, 5))