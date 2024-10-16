"""
fraction structure:
2/3 -> [2,3]

"""


def fractionMuliplication(fraction1,fraction2):
    if fraction1[0]==0:
        return [0,0]
    
    if fraction2[0]==0:
        return [0,0]
    
    if fraction1[1]==0:
        print("Error: zerro divison")
        return [0,0]
    
    if fraction2[1]==0:
        print("Error: zerro divison")
        return [0,0]
    
    return [fraction1[0]*fraction2[0],fraction1[1]*fraction2[1]]

def bruteForceFractionAddison(fraction1,fraction2):
    if fraction1[0]==0:
        return fraction2
    
    if fraction2[0]==0:
        return fraction1
    
    if fraction1[1]==fraction2[1]:
        commonFactor = fraction1[1]
        topFactor1 = 1
        topFactor2 = 1
    else:
        commonFactor = fraction1[1]*fraction2[1]

        topFactor1 = fraction2[1]
        topFactor2 = fraction1[1]
    
    newFraction1 = [fraction1[0]*topFactor1,commonFactor]
    newFraction2 = [fraction2[0]*topFactor2,commonFactor]
    returnFraction = [newFraction1[0]+newFraction2[0],commonFactor]
    return returnFraction


def fractionToNumb(fraction):
    if fraction ==[0,0]:
        return 0
    return fraction[0]/fraction[1]

if __name__ == "__main__":
    print("hei")
    print(fractionMuliplication([3,1],[-3,1]))