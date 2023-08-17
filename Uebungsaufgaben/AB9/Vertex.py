class Vertex:
    """
    Vertex class
    """

    def __init__(self, x, y, z):
        """
        Constructor
        :param x: x value
        :param y: y value
        :param z: z value
        """

        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __repr__(self):
        return "Vertex x={} y={} z={}".format(self.x, self.y, self.z)
