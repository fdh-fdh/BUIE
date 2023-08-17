from Vertex import Vertex


class Face:

    def __init__(self, v1, v2, v3):
        self.v1: Vertex = v1
        self.v2: Vertex = v2
        self.v3: Vertex = v3

    def show(self, ax, style="-xk"):
        ax.plot3D([self.v1.x, self.v2.x], [self.v1.y, self.v2.y], [self.v1.z, self.v2.z], style)
        ax.plot3D([self.v2.x, self.v3.x], [self.v2.y, self.v3.y], [self.v2.z, self.v3.z], style)
        ax.plot3D([self.v3.x, self.v1.x], [self.v3.y, self.v1.y], [self.v3.z, self.v1.z], style)



