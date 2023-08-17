import geo_element3d as iiid
import math as mt


class cylinder(iiid.geo_element3d):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def calc_volume(self):
        return self.height * mt.pi * self.radius * self.radius
