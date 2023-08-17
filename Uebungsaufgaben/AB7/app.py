from BRep import BRep
from Face import Face
from Vertex import Vertex

# main script

# face1 = Face(v1=Vertex(0, 0, 0), v2=Vertex(2, 3, 5), v3=Vertex(2, 0, 0))
# print(face1)

geometry = BRep.from_STL(filename="bunny.stl")

geometry.show_3d()

geometry.to_STL("geometry")

Cob = BRep.create_cuboid(2,2,4,s=3)
Cob.show_3d()