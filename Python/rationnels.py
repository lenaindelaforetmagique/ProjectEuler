from math import gcd, log10

class Rationnel:
    """
#Classe de nombres rationnels
X. Morin - 05/2017
Rationnel = a/b (avec a et b entiers relatifs)

Operateurs implémentés: (q : Rationnel, z : entier relatif)
"+" : q+q, q+z, z+q, q+=q, q+=z, z+=q
"-" : q-q, q-z, z-q, q-=q, q-=z, z-=q
"*" : q*q, q*z, z*q, q*=q, q*=z, z*=q
"/" : q/q, q/z, z/q, q/=q, q/=z, z/=q

"""
    def __init__(self,numerator=0, denominator=1):
        #Filtre
        decMax = 22
        l1 = int(log10(max(abs(numerator),1)))+1
        l2 = int(log10(abs(denominator)))+1
        if max(l1, l2) > decMax:
            div = 10**(max(l1, l2)-decMax)
            numerator //= div
            denominator //= div
        
        g = gcd(numerator,denominator)
        numerator //= g
        denominator //= g
        if numerator*denominator > 0:
            a = 1
        else:
            a = -1
        self.num = a*abs(numerator)
        self.den = abs(denominator)
        
    def __repr__(self):
        return str(self.num) + '/' + str(self.den)

    def __add__(self, other):
        if type(other) == Rationnel:
            a = self.num*other.den + self.den*other.num
            b = self.den*other.den
            return Rationnel(a,b)
        elif type(other) == int:
            return self+Rationnel(other)
        else:
            return NotImplemented

    def __radd__(self, other):
        return self+other

    def __iadd__(self, other):
        return self+other
            
    def __sub__(self, other):
        if type(other) == Rationnel:
            a = self.num*other.den - self.den*other.num
            b = self.den*other.den
            return Rationnel(a,b)
        elif type(other) == int:
            return self-Rationnel(other)
        else:
            return NotImplemented
        
    def __rsub__(self, other):
        if type(other) == int:
            return Rationnel(other)-self
        else:
            return NotImplemented

    def __isub__(self, other):
        return self-other

    def __mul__(self, other):
        if type(other) == Rationnel:
            a = self.num*other.num
            b = self.den*other.den
            return Rationnel(a,b)
        elif type(other) == int:
            a = self.num*other
            b = self.den
            return Rationnel(a,b)
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self*other
    
    def __imul__(self, other):
        return self*other

    def __truediv__(self, other):
        if type(other) == Rationnel:
            a = self.num*other.den
            b = self.den*other.num
            return Rationnel(a,b)
        elif type(other) == int:
            a = self.num
            b = self.den*other
            return Rationnel(a,b)
        else:
            return NotImplemented

    def __rtruediv__(self, other):
        if type(other) == int:
            return Rationnel(other)/self
        else:
            return NotImplemented

    def __itruediv__(self, other):
        return self/other
        
    def __lt__(self, other):
        if type(other) == Rationnel:           
            return self.num*other.den < other.num*self.den
        elif type(other) == int:
            return self.num < other*self.den
        else:
            return NotImplemented

    def __le__(self, other):
        if type(other) == Rationnel:           
            return self.num*other.den <= other.num*self.den
        elif type(other) == int:
            return self.num <= other*self.den
        else:
            return NotImplemented

    def __eq__(self, other):
        if type(other) == Rationnel:
            return (self.num == other.num) and (self.den == other.den)
        elif type(other) == int:
            return (self.den == 1) and (self.num == other)
        else:
            return NotImplemented
    
    def __ne__(self, other):
        if type(other) == Rationnel:
            return (self.num != other.num) or (self.den != other.den)
        elif type(other) == int:
            return (self.den != 1) or (self.num != other)
        else:
            return NotImplemented

    def __gt__(self, other):
        if type(other) == Rationnel:           
            return self.num*other.den > other.num*self.den
        elif type(other) == int:
            return self.num > other*self.den
        else:
            return NotImplemented

    def __ge__(self, other):
        if type(other) == Rationnel:           
            return self.num*other.den >= other.num*self.den
        elif type(other) == int:
            return self.num >= other*self.den
        else:
            return NotImplemented

    

if __name__ == "__main__":
    v1 = Rationnel(1,3)
    v2 = Rationnel(3,5)
    print(v1, v2)
    print("add",v1+v2)
    print("sub",v1-v2)
    print("mul1",v1*v2)
    print("mul2",5*v1)
    print("mul2",v1*5)
    print("div", v1/v2)
    print("div", v2/v1)
    print("div2", 12/v1)
    print("div2", v1/12)
   
    v1 += 2
    print(v1)
    a = 2
    a += v1
    print(a)

    print("tests comparateurs")
    a = 2
    print(a, v1, a>=v1)
    print(v1, v2, v1>=v2)
    





