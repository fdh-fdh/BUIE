import Cuboid as cb
import Cube as cu
import Cylinder as cy


a = cb.cuboid(5, 8, 0.5)
vol = a.calc_volume()
print(vol)

b = cu.cube(4, 4, 4)
vol_cube = b.calc_volume()
print(vol_cube)
# da superklasse schon ein vol methode definiert hatte, als untere klasse werden die methoden der
# superklasse übernommen.

c = cy.cylinder(1,10)
vol_cy = c.calc_volume()
print(vol_cy)

obj = [a,b,c]
obj_vol = 0
for i in range(1,3):
    obj_vol = obj_vol+obj[i].calc_volume()

print(obj_vol)