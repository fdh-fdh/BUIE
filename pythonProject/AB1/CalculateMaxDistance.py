import numpy as np
import matplotlib.pyplot as plt
# inizialisierung
n = np.array(np.zeros(10))
#random zahlen speichern
for i in range(1,10):
    n[i] = np.random.randint(0,100)

print(n[:])

#umkehrung
n_umkehr =n[::-1]
print(n_umkehr)
#abstand suchen
abstand = np.array(np.zeros(9))
for i in range(0,9):
    abstand[i] = abs(n[i]-n[i+1])

a=np.min(abstand)
b= np.max(abstand)
print(abstand)
print(a)
print(b)

