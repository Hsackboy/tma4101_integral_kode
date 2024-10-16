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
        # print(f"{newPoly[i]}= {poly1[i]}+{poly2[i]}")
    return newPoly

def gange_polinominal(poly1,poly2):
    if len(poly1)>len(poly2):
        mainPoly = poly1
        secondaryPoly = poly2
    else:
        secondaryPoly = poly1
        mainPoly = poly2
    
    newPoly =createEmtyPolynominal(len(poly1)+len(poly2)-1)
    
    for i in range(len(mainPoly)):
        for j in range(len(secondaryPoly)):
            newFactor = fL.fractionMuliplication(mainPoly[i],secondaryPoly[j])
            # print(f"{mainPoly[i]}*{secondaryPoly[j]}= {newFactor},x^{i+j}")
            newPoly[i+j] =fL.bruteForceFractionAddison(newPoly[i+j],newFactor)
    
    return newPoly
    
    

def print_poly(poly,writeAsFractions = True):
    printString = ""
    if writeAsFractions:
        for i in range(len(poly)):
            reversedIndex = len(poly)-1-i
            printString += f"{poly[reversedIndex][0]}/{poly[reversedIndex][1]}*x^{reversedIndex} + "
        print(printString[:-2])
    else:
        for i in range(len(poly)):
            reversedIndex = len(poly)-1-i
            printString += f"{fL.fractionToNumb(poly[reversedIndex])}*x^{reversedIndex} + "
        print(printString[:-2])


def polyStringToFunction(poly,x):
    fVal = 0
    for i in range(len(poly)):
        fVal+=fL.fractionToNumb(poly[i])*(x**i)
    return fVal
        
    

def bestemtIntegralPolynom(poly,a,b):
    integrertPolynom = createEmtyPolynominal(len(poly)+1)
    # print(len(integrertPolynom))
    for i in range(len(integrertPolynom)-1):
        integrertPolynom[i+1]= fL.fractionMuliplication(poly[i],[1,i+1])
        # print(f"{poly[i]}*{[1,i+1]} = {fL.fractionMuliplication(poly[i],[1,i+1])}")
    return polyStringToFunction(integrertPolynom,b)-polyStringToFunction(integrertPolynom,a)
    

if __name__ == "__main__":
    print("hei")
    # poly1 = [[-6,-6],[11,-6],[-6,-6],[1,-6]]
    # poly2 = [[0,-2],[3,-2],[-4,-2],[1,-2]]
    # poly3 = [[0,6],[4,6],[-6,6],[2,6]]

    # print_poly(poly1)
    # print_poly(poly2)
    # print_poly(poly3)

    # print_poly(pluss_polinominal(poly3,pluss_polinominal(poly1,poly2)))
    
    #(1/-2*x^1 + -2/-2*x^0 ) * (1/-1*x^1 + -1/-1*x^0 )
    
    
    print(fL.bruteForceFractionAddison([-1,2],[-2,2]))
    
    poly1 =[[-2,-2],[1,-2]]
    poly2 =[[-1,-1],[1,-1]]
    
    print_poly(poly1)
    print("")
    print_poly(poly2)
    print("")
    
    print("")
    print_poly(gange_polinominal(poly1,poly2))