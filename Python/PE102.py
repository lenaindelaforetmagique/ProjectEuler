"""Problem 102

Three distinct points are plotted at random on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000, such that a triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.

Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing the co-ordinates of one thousand "random" triangles, find the number of triangles for which the interior contains the origin.

NOTE: The first two examples in the file represent the triangles in the example given above."""


fichier=open('PE102_triangles.txt','r')
lignes=fichier.readlines()
fichier.close()



def contient_origine(l):
    pv1 = l[0]*l[3]-l[2]*l[1]
    pv2 = l[2]*l[5]-l[4]*l[3]
    pv3 = l[4]*l[1]-l[0]*l[5]
    return pv1 * pv2 > 0 and pv1 * pv3 >0

s = 0
for ligne in lignes:
    tgle = ligne[:-1].split(',')
    for i,c in enumerate(tgle):
        tgle[i] = int(c)
    if contient_origine(tgle):
        s += 1


print(s)



    
