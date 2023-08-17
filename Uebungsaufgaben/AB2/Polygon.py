import numpy as np
n = 0
#Anzahl der eckpunkt
while n < 3:
    n = int(input('Geben Sie die Anzahl der Eckpunkten:'))
    if n <3 :
        print('um Polygon sinnvoll zu zeichnen müssen mind. 3 Punkten eingegeben werden! ')

#inizialisierung der eckpunkt matrix

p = np.zeros((n,2),dtype=int)
print(p)

#koordinaten einlesen

for i in range(0,n):
    p[i,0] = int(input('Geben Sie die x Koordinaten der {}. Punkte: '.format(i+1)))
    p[i,1] = int(input('Geben Sie die y  Koordinaten der {}. Punkte: '.format(i+1)))

print('This is your points of Polygon\n {}'.format(p))
#Reshape
add_=p[1,:]
p=np.row_stack((p, add_))



#Flächen und Umfang berechnen
A = 0
U = 0
for i in range(0,n):
    U = U + (((p[(i+1),0]-p[i,0])^2) + ((p[(i+1),1]-p[i,1])^2))**0.5
    A =0.5*(p[(i+1),0]-p[i,0])*(p[(i+1),1]+p[i,1])

print(U)
print(A)

if A > 0:
    print('Flächeninhalt Positiv, in Uhrzeigersinn eingegeben')
else:
    if A < 0:
        print('Flächeninhalt Negativ, in Gegenuhrzeigersinn eingegeben.')

