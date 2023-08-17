import Vertex as V


class Brep:
    def __init__(self, faces):
        self.faces = faces

    @classmethod
    def from_STL(cls, filename):
        with open(filename) as f:
            text = f.read()

        lines = text.split(sep="\n")
        lines = lines[1:-2]

        num_lines = len(lines)
        num_faces = num_lines / 7

        for i in range(0, num_lines, 7):
            row_vertex_1 = lines[i + 2].split()[1:3]
            row_vertex_2 = lines[i + 3].split()[1:3]
            row_vertex_3 = lines[i + 4].split()[1:3]

            vertex_1 = V.Vertex(*row_vertex_1)
            vertex_2 = V.Vertex(*row_vertex_2)
            vertex_3 = V.Vertex(*row_vertex_3)
