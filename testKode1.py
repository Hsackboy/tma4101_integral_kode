import math as m
import lagrangepolynomLib as LPL
import polynomMatte as pM

def f(x):
    return (1/m.sqrt(2*m.pi))*(m.e**(-((x**2)/2))) *100


points = []
pointAmount = 7
startPoint = 0
endpoint = 1
steg = (endpoint-startPoint)/(pointAmount-1)

for i in range(pointAmount):
    points.append((i*steg,f(i*steg)))

print( points)

larangeFunk = LPL.lagrangepolynom(points)

pM.print_poly(larangeFunk,False)
print(pM.bestemtIntegralPolynom(larangeFunk,startPoint,endpoint))