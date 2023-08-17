import numpy as np
from matplotlib import pyplot as plt

from triangles import *

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

T1 = triangle_1
T2 = triangle_5

T1.show(ax, style="-r")
T2.show(ax, style="-g")

plt.show()

V0_1 = np.array([T1.v1.x, T1.v1.y, T1.v1.z])
V1_1 = np.array([T1.v2.x, T1.v2.y, T1.v2.z])
V2_1 = np.array([T1.v3.x, T1.v3.y, T1.v3.z])

V0_2 = np.array([T2.v1.x, T2.v1.y, T2.v1.z])
V1_2 = np.array([T2.v2.x, T2.v2.y, T2.v2.z])
V2_2 = np.array([T2.v3.x, T2.v3.y, T2.v3.z])

# Ebenengleichung für pi2
N2 = np.cross((V1_2 - V0_2), (V2_2 - V0_2))
N2 = N2 / np.linalg.norm(N2)
d2 = np.dot(-N2, V0_2)

# Abstände der Knoten Dreieck 1 zu Ebene pi2
dV0_1 = np.dot(N2, V0_1) + d2
dV1_1 = np.dot(N2, V1_1) + d2
dV2_1 = np.dot(N2, V2_1) + d2

# Ebenengleichung für pi1
N1 = np.cross((V1_1 - V0_1), (V2_1 - V0_1))
N1 = N1 / np.linalg.norm(N1)
d1 = np.dot(-N1, V0_1)

# Abstände der Knoten Dreieck 2 zu Ebene pi1
dV0_2 = np.dot(N1, V0_2) + d1
dV1_2 = np.dot(N1, V1_2) + d1
dV2_2 = np.dot(N1, V2_2) + d1

# alle Knoten von Dreieck 1 über oder unter Ebene pi2?
if (dV0_1 < 0 and dV1_1 < 0 and dV2_1 < 0) or (dV0_1 > 0 and dV1_1 > 0 and dV2_1 > 0):
    print("Triangles do not intersect. ")
    exit()

# alle Knoten von Dreieck 2 über oder unter Ebene pi1?
if (dV0_2 < 0 and dV1_2 < 0 and dV2_2 < 0) or (dV0_2 > 0 and dV1_2 > 0 and dV2_2 > 0):
    print("Triangles do not intersect. ")
    exit()

# Dreiecke konplanar?
if dV0_1 == 0 and dV1_1 == 0 and dV2_1 == 0:
    print("Triangles are co-planar. ")
    exit()


D = np.cross(N1, N2)

pV0_1 = np.dot(D, V0_1)
pV1_1 = np.dot(D, V1_1)
pV2_1 = np.dot(D, V2_1)

# we don't need O at this time because we are
# interested in whether its overlapped or not. not for
# concrete quantity.

t1 = pV0_1 + (pV1_1-pV0_1)*dV0_1/(dV0_1-dV1_1)
t2 = pV2_1 + (pV2_1-pV1_1)*dV2_1/(dV2_1-dV1_1)

V0_1V1_1 = np.array([(V1_1[0]-V0_1[0]), (V1_1[1]-V0_1[1]), (V1_1[2]-V0_1[2])])
V1_1V2_1 = np.array([(V2_1[0]-V1_1[0]), (V2_1[1]-V1_1[1]), (V2_1[2]-V1_1[2])])

V0_1V1_1 = V0_1V1_1 / np.linalg.norm(V0_1V1_1)
V1_1V2_1= V1_1V2_1 / np.linalg.norm(V1_1V2_1)
D = D / np.linalg.norm(D)


if (D[0]== V0_1V1_1[0], D[1]== V0_1V1_1[1]) or (D[0]== V1_1V2_1[0], D[1]== V1_1V2_1[1]):
    print("VO1 V12 NOT at THE SAME SIDE")
else:
    print("at the same side")
