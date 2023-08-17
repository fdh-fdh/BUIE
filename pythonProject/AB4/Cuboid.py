import geo_element3d as iiid


class cuboid(iiid.geo_element3d):
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def calc_volume(self):
        return self.height * self.width * self.length

