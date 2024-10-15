"""
polinomStruktur:
[[2,3],[4,5],[5,1]] ->
2/3 x^0 +4/5 x^1 + 5/1 x^2
"""

import fractionLib as fL


def createEmtyPolynominal(degree):
    return [[0,0] for i in range(degree)]



def pluss_polinominal(poly1,poly2):
    if len(poly1)>len(poly2):
        mainPoly = poly1
        secondaryPoly = poly2
    else:
        secondaryPoly = poly1
        mainPoly = poly2
    
    newPoly = mainPoly.copy()
    
    for i in range(len(secondaryPoly)):
        newPoly[i] = fL.bruteForceFractionAddison(poly1[i],poly2[i])
        print(f"{newPoly[i]}= {poly1[i]}+{poly2[i]}")
    return newPoly

def print_poly(poly):
    printString = ""
    for i in range(len(poly)):
        reversedIndex = len(poly)-1-i
        printString += f"{poly[reversedIndex][0]}/{poly[reversedIndex][1]}*x^{reversedIndex} + "
    print(printString[:-2])


if __name__ == "__main__":
    print("hei")
    poly1 = [[-6,-6],[11,-6],[-6,-6],[1,-6]]
    poly2 = [[0,-2],[3,-2],[-4,-2],[1,-2]]
    poly3 = [[0,6],[4,6],[-6,6],[2,6]]

    print_poly(poly1)
    print_poly(poly2)
    print_poly(poly3)

    print_poly(pluss_polinominal(poly3,pluss_polinominal(poly1,poly2)))