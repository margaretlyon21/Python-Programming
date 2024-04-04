from fractions import Fraction
def gcd(a, b):

    if(b == 0):
        return abs(a)
    else:
        return gcd(b, a % b)

def egypt(p,q):
    """
     >>> egypt(3,4)
     1/2 + 1/4
     >>> egypt(11,12)
     1/2 + 1/3 + 1/12
     
     >>> egypt(123,124)
     1/2 + 1/3 + 1/7 + 1/64 + 1/8333 + 1/347186112
     >>> egypt(103,104)
     1/2 + 1/3 + 1/7 + 1/71 + 1/9122 + 1/141449381 + 1/100039636784966424
     """
    def listofunitfractions(p, q, lst):
        numerator = p
        denominator = q
        while True:
            divis = denominator // numerator
            mod = denominator % numerator
        
            if mod > 0:
                unitdenom = divis + 1
            else:
                unitdenom = divis
            
            lst.append((unitdenom))
            numerator = int((unitdenom * numerator) - (1 * denominator))
            denominator = int((unitdenom * denominator))

            if (gcd(numerator, denominator) != 1):
                numerator1 = numerator
                numerator = int(numerator / gcd(numerator,denominator))
                denominator = int(denominator / gcd(numerator1,denominator))  

            if numerator == 1:
                lst.append(denominator)
  
                return(lst)
    unitfracs = []
    listofunitfractions(p,q,unitfracs)
   
    i = 1
    for item in unitfracs:
        num = str(Fraction(1,int(item)))
        print(str(num),end="")
        if (i < len(unitfracs)):
            i +=1
            print(" + ", end="")
   
import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)