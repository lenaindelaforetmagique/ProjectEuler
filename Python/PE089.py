"""Problem 89

For a number written in Roman numerals to be considered valid there are basic rules which must be followed.
Even though the rules allow some numbers to be expressed in more than one way there is always a "best" way of writing a particular number.

For example, it would appear that there are at least six ways of writing the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be the most efficient, as it uses the least number of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in valid, but not necessarily minimal, Roman numerals; see About... Roman Numerals for the definitive rules for this problem.

Find the number of characters saved by writing each of these in their minimal form.

Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.
"""
import os.path
cwd = os.path.split(__file__)[0]
fichier = open(os.path.join(cwd, 'PE089_roman.txt'), 'r')
L = fichier.readlines()
fichier.close()

# print(L)


# liste=["13\n2","uio","poop","pppp"]

def reduction(L):
    L = "IV".join(L.split("IIII"))
    L = "IX".join(L.split("VIV"))
    L = "XL".join(L.split("XXXX"))
    L = "XC".join(L.split("LXL"))
    L = "CD".join(L.split("CCCC"))
    L = "CM".join(L.split("DCD"))
    return L


def arabic_Roman(a):
    L = "".join('I' * a)
    L = "V".join(L.split("IIIII"))
    L = "X".join(L.split("VV"))
    L = "L".join(L.split("XXXXX"))
    L = "C".join(L.split("LL"))
    L = "D".join(L.split("CCCCC"))
    L = "M".join(L.split("DD"))

    L = "IV".join(L.split("IIII"))
    L = "IX".join(L.split("VIV"))
    L = "XL".join(L.split("XXXX"))
    L = "XC".join(L.split("LXL"))
    L = "CD".join(L.split("CCCC"))
    L = "CM".join(L.split("DCD"))

    return L


a = 11996
# print(arabic_Roman(a))

s = 0
for m in L:
    n = reduction(m)
    # print(m)
    # if len(m)!=len(n):
    # print([m,n])
    s += len(m) - len(n)

print(s)
