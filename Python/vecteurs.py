class Vecteur:
    """
#Classe de vecteurs
X. Morin - 05/2017
Vecteur = liste de coordonnées + dim

Operateurs implémentés: (V : Vecteur, a : nombre)
"+" : V+V, V+=V
"-" : V-V, V-=V
"*" : V*V (produit scalaire), V*a, a*V, V*=V, a*=V, V*=a (attention au type retourné)
"""
    def __init__(self, coordinatesList):
        self.dim = len(coordinatesList)
        self.coord = coordinatesList

    def __add__(self, other):
        if type(other) == Vecteur:
            if self.dim == other.dim:
                t = [self.coord[i]+other.coord[i] for i in range(self.dim)]
                return Vecteur(t)
            else:
                print("add - Erreur de dimension")
                return self
                
        else:
            return NotImplemented
            
    def __iadd__(self, other):
        return self+other
    
    def __sub__(self, other):
        if type(other) == Vecteur:
            if self.dim == other.dim:
                t = [self.coord[i]-other.coord[i] for i in range(self.dim)]
                return Vecteur(t)
            else:
                print("sub - Erreur de dimension")
        else:
            return NotImplemented
            
    def __isub__(self, other):
        return self-other

    def __mul__(self, other):
        if type(other) == Vecteur:
            if self.dim == other.dim:
                v = sum([self.coord[i]*other.coord[i] for i in range(self.dim)])
                return v
            else:
                print("mul - Erreur de dimension")
        else:
            t = [other*v for v in self.coord]
            return Vecteur(t)

    def __rmul__(self, other):
        return self*other
    
    def __imul__(self, other):
        return self*other

    def __repr__(self):
        return str(self.coord[0]) + ", " + str(self.coord[1])
    

if __name__ == "__main__":
    v1 = Vecteur([1,2,3])
    v2 = Vecteur([2,9,1])
    print("+", v1+v2)
    print("-", v1-v2)
    print("*", v1*v2)
    print("a*", 12*v1)
    print("*a", v1*13)
    
    

