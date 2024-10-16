import polynomMatte as pM
import fractionLib as fL


def lagrangepolynom(points:list):
    p = [[0,0]]
    for kPoint in points:
        # print(str(points.index(kPoint))+":")
        lk = [[1,1]]
        for jPoint in points:
            if jPoint!=kPoint:
                botfactor =kPoint[0]-jPoint[0]
                poly = [[-jPoint[0],botfactor],[1,botfactor]]
                lk = pM.gange_polinominal(lk,poly)
        
        # print("L"+str(points.index(kPoint))+":")
        # pM.print_poly(lk)
        # print("")
        # print("")
        lk = pM.gange_polinominal(lk,[[kPoint[1],1]])
        # print("L"+str(points.index(kPoint))+"*f(k):")
        # pM.print_poly(lk)
        # print("")
        # print("")
        p = pM.pluss_polinominal(p,lk)
    return p
                
                
        


if __name__=="__main__":
    print("hei")
    points = [(1,1),(2,5),(3,7),(4,-2),(5,-3),(6,7)]
    poly = lagrangepolynom(points)
    
    pM.print_poly(poly)
    pM.bestemtIntegralPolynom(poly,0,0)