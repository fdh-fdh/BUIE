from typing import List

import matplotlib.pyplot as plt
import numpy as np

from Face import Face
from Vertex import Vertex


class BRep:

    def __init__(self, list_of_faces=[]):
        self.faces = list_of_faces

    def show(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        for face in self.faces:
            face.plot_3d(ax)
        plt.show()

    @classmethod
    def from_STL(cls, filename):

        # load file content
        with open(filename, encoding='utf-8') as f:
            text = (f.read())

        # split lines
        lines = text.split("\n")

        # trim first and last item
        lines = lines[1:-2]

        # count lines
        n = len(lines)

        faces = []

        for i in range(0, n, 7):
            # get vertices from text
            raw_vertex_1 = lines[i + 2].split()[1:]
            raw_vertex_2 = lines[i + 3].split()[1:]
            raw_vertex_3 = lines[i + 4].split()[1:]

            # create vertex instances by unpacking the list
            vertex_1 = Vertex(*raw_vertex_1)
            vertex_2 = Vertex(*raw_vertex_2)
            vertex_3 = Vertex(*raw_vertex_3)

            # instantiate Facet
            face = Face(v1=vertex_1, v2=vertex_2, v3=vertex_3)

            # append to global list
            faces.append(face)

        return cls(faces)

    def to_STL(self, filename):
        output = ['solid ASCII\n']
        for face in range(len(self.faces)):
            normal = self.faces[face].normal
            output.append('  facet normal {:e} {:e} {:e}\n'.format(normal[0], normal[1], normal[2]))

            output.append('    outer loop\n')
            output.append("      vertex   {:e} {:e} {:e}\n".format(self.faces[face].v1.x, self.faces[face].v1.y,
                                                                   self.faces[face].v1.z))
            output.append("      vertex   {:e} {:e} {:e}\n".format(self.faces[face].v2.x, self.faces[face].v2.y,
                                                                   self.faces[face].v2.z))
            output.append("      vertex   {:e} {:e} {:e}\n".format(self.faces[face].v3.x, self.faces[face].v3.y,
                                                                   self.faces[face].v3.z))
            output.append('    endloop\n')
            output.append('  endfacet\n')
        output.append('endsolid\n')
        output = ''.join(output)
        file = open(filename, "w", encoding="utf-8")
        file.write(output)
        file.close()

    @classmethod
    def create_cuboid(cls, center=[0, 0, 0], side_length=[1, 1, 1]):
        """

        :param center:
        :param side_length:
        :return:
        """

        vertices = []
        for i in -1, 1:
            for j in -1, 1:
                for k in -1, 1:
                    vertices.append(Vertex(center[0] + 0.5 * i * side_length[0], center[1] + 0.5 * j * side_length[1],
                                           center[2] + 0.5 * k * side_length[2]))

        points = ['013', '032', '041', '145', '062', '046', '465', '567', '273', '267', '153', '357']
        faces = []

        for i in range(12):
            faces.append(Face(vertices[int(points[i][0])], vertices[int(points[i][1])], vertices[int(points[i][2])]))
        return cls(faces)

    def project_onto_xz_plane(self):
        """
        projects all points onto the xz plane
        :return:
        """
        for face in self.faces:
            face.v1.y = 0
            face.v2.y = 0
            face.v3.y = 0

    def get_min_max(self) -> tuple:
        """
        returns the minimal and maximal values for x, y, z
        :return:
        """
        x_min = self.faces[0].v1.x
        y_min = self.faces[0].v1.y
        z_min = self.faces[0].v1.z
        x_max = self.faces[0].v1.x
        y_max = self.faces[0].v1.y
        z_max = self.faces[0].v1.z
        for i in self.faces:
            x=[i.v1.x,i.v2.x,i.v3.x]
            max_x= np.max(x)
            min_x= np.min(x)

            if max_x > x_max:
                x_max= max_x
            if min_x < x_min:
                x_min = min_x

            y=[i.v1.y,i.v2.y,i.v3.y]
            max_y = max(y)
            min_y = min(y)

            if max_y> y_max:
                y_max = max_y
            if min_y < y_min:
                y_min = min_y

            z=[i.v1.z,i.v2.z,i.v3.z]
            max_z = max(z)
            min_z = min(z)

            if max_z > z_max:
                z_max = max_z
            if min_z < z_min:
                z_min = min_z

        return x_min, x_max, y_min, y_max, z_min, z_max

    def move_to_origin(self, x, y, z) -> None:
        """
        moves the BRep geometry by the specified x, y, z
        :param x:
        :param y:
        :param z:
        :return:
        """
        for i in self.faces:
            i.v1.x = i.v1.x-x
            i.v1.y = i.v1.y-y
            i.v1.z = i.v1.z-z
            i.v2.x = i.v2.x-x
            i.v2.y = i.v2.y-y
            i.v2.z = i.v2.z-z
            i.v3.x = i.v3.x-x
            i.v3.y = i.v3.y-y
            i.v3.z = i.v3.z-z

    def apply_backface_culling(self) -> List:
        """
        returns only those triangles that must be considered in the rasterization
        :return:
        """

        flist_bc = []  # neue Liste, die nur die Dreiecke enthält, die weiter betrachtet werden müssen
        camera_pos = np.transpose(np.array([0,1,0]))
        for i in self.faces:
            norm = i.get_normal()
            if np.dot(norm, camera_pos) >= 0:
                flist_bc.append(i)
        return flist_bc
