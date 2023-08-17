import numpy as np

from Vertex import Vertex
from matplotlib.path import Path


class Face:
    """
    Face class
    """

    def __init__(self, v1, v2, v3):
        """
        Face constructor
        :param v1:
        :param v2:
        :param v3:
        """
        self.v1: Vertex = v1
        self.v2: Vertex = v2
        self.v3: Vertex = v3

    def plot_3d(self, ax, style='-k'):
        """
        adds this face to a plot
        :param style:
        :param ax: subplot area to be printed into
        :return: nothing
        """
        ax.plot3D([self.v1.x, self.v2.x], [self.v1.y, self.v2.y], [self.v1.z, self.v2.z], style)
        ax.plot3D([self.v2.x, self.v3.x], [self.v2.y, self.v3.y], [self.v2.z, self.v3.z], style)
        ax.plot3D([self.v3.x, self.v1.x], [self.v3.y, self.v1.y], [self.v3.z, self.v1.z], style)

    def get_normal(self):
        """
        calculates the normal vector based on the three vertices that specify this face
        :return
        """
        vertex1 = np.array([self.v1.x ,self.v1.y , self.v1.z])
        vertex2 = np.array([self.v2.x ,self.v2.y , self.v2.z])
        vertex3 = np.array([self.v3.x ,self.v3.y , self.v3.z])
        v1=np.array([(vertex1[0]-vertex2[0]),(vertex1[1]-vertex2[1]),(vertex1[2]-vertex2[2])])
        v2=np.array([(vertex1[0]-vertex3[0]),(vertex1[1]-vertex3[1]),(vertex1[2]-vertex3[2])])
        norme = np.cross(v1,v2)
        return norme/np.linalg.norm(norme)


    def point_in_projected_face(self, px: Vertex):
        """
        returns True if given point px is inside
        :param px: an instance of the Vertex class
        :return: boolean
        """

        p1 = self.v1
        p2 = self.v2
        p3 = self.v3

        projected_vertices = [(p1.x, p1.z),
                              (p2.x, p2.z),
                              (p3.x, p3.z)
                              ]

        polygon = Path(vertices=projected_vertices)

        return polygon.contains_point((px.x, px.z))
