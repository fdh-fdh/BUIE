import xml.dom.minidom
import matplotlib.pyplot as pyplt


class wall:
    def __init__(self, name):
        self.name = name
        self.x=[]
        self.y=[]


doc = xml.dom.minidom.parse("floorplan.xml")


wall_list = []
for Wall in doc.getElementsByTagName("Wall"):
    name = Wall.getElementsByTagName("Name")[0].firstChild.data
    W = wall(name)
    wall_list.append(W)
    print("\nWall" + W.name + " has following Points: ")
    for rep in Wall.getElementsByTagName("Representation"):
        for points in rep.getElementsByTagName("Point"):
            x_ = points.getElementsByTagName("x")[0]
            x1 = x_.getAttribute("val")
            y_ = points.getElementsByTagName("y")[0]
            y1 = y_.getAttribute("val")
            W.x.append(x1)
            W.y.append(y1)
            print("\nx=" + x1 + "\ny=" + y1)

for wall in wall_list:
    wall_visual = pyplt.plot(wall.x, wall.y)

    pyplt.show()



