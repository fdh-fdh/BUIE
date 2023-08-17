from Vertex import Vertex
from Face import Face

v_1 = Vertex(0, 0, 0)
v_2 = Vertex(0, 0, 3)
v_3 = Vertex(2, 0, 0)

v_4 = Vertex(1, 1, 1)
v_5 = Vertex(4, 1, 1)
v_6 = Vertex(1, 2, 1)

v_7 = Vertex(0, 0, 0)
v_8 = Vertex(1, 0, 0)
v_9 = Vertex(0, 0, 4)

v_10 = Vertex(-1, 1, 1)
v_11 = Vertex(0, -1, 0)
v_12 = Vertex(2, 2, 1)

v_13 = Vertex(0, 1, 1)
v_14 = Vertex(2, -1, 1)
v_15 = Vertex(-2, -1, 1)

v_21 = Vertex(3, 0, -1)
v_22 = Vertex(0, 0, 2)
v_23 = Vertex(0, 0, -1)

v_24 = Vertex(-1, -1, 0)
v_25 = Vertex(-1, 3, 0)
v_26 = Vertex(3, -1, 0)

triangle_1 = Face(v_1, v_2, v_3)
triangle_2 = Face(v_4, v_5, v_6)
triangle_3 = Face(v_7, v_8, v_9)
triangle_4 = Face(v_10, v_11, v_12)
triangle_5 = Face(v_13, v_14, v_15)
triangle_6 = Face(v_21, v_22, v_23)
triangle_7 = Face(v_24, v_25, v_26)
