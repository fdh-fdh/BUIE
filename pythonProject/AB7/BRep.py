from matplotlib import pyplot as plt

from Face import Face
from Vertex import Vertex


class BRep:

    def __init__(self, faces):
        self.faces = faces

    def to_STL(self, name:str):
        with open(name+".stl", 'w') as f:
            f.write('solid ASCII\n')
            for i in self.faces:
                vertex1 = i.v1
                vertex2 = i.v2
                vertex3 = i.v3
                A= [vertex1.x-vertex2.x, vertex1.y-vertex2.y, vertex1.x-vertex2.z]
                B =[vertex2.x-vertex3.x, vertex2.y-vertex3.y, vertex2.x-vertex3.z]
                norm = [A[1]*B[2]-A[2]*B[1], A[2]*B[0]-A[0]*B[2], A[0]*B[1]-A[1]*B[0]]
                f.write('facet normal ' + "{:.2e}".format(norm[0]) + "{:.2e}".format(norm[1]) + ' ' + "{:.2e}".format(norm[2])+ "\n")
                for j in [vertex1, vertex2,vertex3]:
                    f.write('vertex   ')
                    f.write("{:.2e}".format(j.x))
                    f.write(' ')
                    f.write("{:.2e}".format(j.y))
                    f.write(' ')
                    f.write("{:.2e}".format(j.z) + '\n')
                f.write("endloop\n")
                f.write("endfacet\n")

            f.write('endsolid')


    @classmethod
    def from_STL(cls, filename):

        with open(filename) as f:
            text = f.read()

        lines = text.split(sep="\n")
        lines = lines[1:-2]

        num_lines = len(lines)
        num_faces = num_lines/7

        faces = []

        for i in range(0, num_lines, 7):
            raw_vertex_1 = lines[i+2].split()[1:]
            raw_vertex_2 = lines[i+3].split()[1:]
            raw_vertex_3 = lines[i+4].split()[1:]

            vertex_1 = Vertex(*raw_vertex_1)
            vertex_2 = Vertex(*raw_vertex_2)
            vertex_3 = Vertex(*raw_vertex_3)

            face = Face(v1=vertex_1, v2=vertex_2, v3=vertex_3)
            faces.append(face)

        return cls(faces=faces)

    def show_3d(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")

        for face in self.faces:
            face.show(ax)

        plt.show()


    @classmethod
    def create_cuboid(cls, x=0, y=0,z=0,s=1):

        M = [[x+0.5*s,y+0.5*s, z+0.5*s],[x+0.5*s,y-0.5*s,z-0.5*s],[x+0.5*s,y-0.5*s,z+0.5*s],[x+0.5*s,y+0.5*s,z-0.5*s],[x-0.5*s,y-0.5*s,z-0.5*s],[x-0.5*s,y-0.5*s,z+0.5*s],[x-0.5*s,y+0.5*s,z-0.5*s],[x-0.5*s,y+0.5*s,z+0.5*s],]
        vertex_list = []
        for i in M:
            vertex = Vertex(i[0],i[1],i[2])
            vertex_list.append(vertex)


        # facet bauen
        faces = []
        Face1 = Face(vertex_list[0],vertex_list[1],vertex_list[3])
        Face2 = Face(vertex_list[1],vertex_list[3],vertex_list[2])
        Face3 = Face(vertex_list[2],vertex_list[5],vertex_list[4])
        Face4 = Face(vertex_list[1],vertex_list[4],vertex_list[2])
        Face5 = Face(vertex_list[3],vertex_list[6],vertex_list[0])
        Face6 = Face(vertex_list[0],vertex_list[7],vertex_list[6])
        Face7 = Face(vertex_list[2],vertex_list[0],vertex_list[5])
        Face8 = Face(vertex_list[5],vertex_list[7],vertex_list[1])
        Face9 = Face(vertex_list[5],vertex_list[6],vertex_list[7])
        Face10 = Face(vertex_list[4],vertex_list[5],vertex_list[6])
        Face11 = Face(vertex_list[1],vertex_list[3],vertex_list[4])
        Face12 = Face(vertex_list[4],vertex_list[3],vertex_list[6])
        faces.append(Face1)
        faces.append(Face2)
        faces.append(Face3)
        faces.append(Face4)
        faces.append(Face5)
        faces.append(Face6)
        faces.append(Face7)
        faces.append(Face8)
        faces.append(Face9)
        faces.append(Face10)
        faces.append(Face11)
        faces.append(Face12)

        return cls(faces=faces)














