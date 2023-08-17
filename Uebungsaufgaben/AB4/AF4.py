from abc import ABC,abstractmethod
import math as mt


class geo_element(ABC):
    pass


class geo_element2d(geo_element):
    @abstractmethod
    def calc_area(self):
        pass

    @abstractmethod
    def calc_perimeter(self):
        pass


class circle(geo_element2d):
    def __init__(self,radius):
        self.radius = radius

    def calc_area(self):
        return mt.pi * self.radius * self.radius

    def calc_perimeter(self):
        return 2* mt.pi * self.radius


class rectangle(geo_element2d):
    def __init__(self,length, height):
        self.length = length
        self.height =  height

    def calc_area(self):
        return self.length*self.height

    def calc_perimeter(self):
        return 2* (self.length + self.height)


class rectangularTriangle(geo_element2d):
    def __init__(self,leg_a, leg_b):
        self.leg_a = leg_a
        self.leg_b = leg_b

    def calc_area(self):
        return self.leg_a*self.leg_b * 0.5

    def calc_perimeter(self):
        return self.leg_a + self.leg_b + mt.sqrt(self.leg_a^2 + self.leg_b^2)


class square(rectangle):
    def __init__(self, length):
        super().__init__(self, length,length)

    def calc_area(self):
        return self.length * self.length

    def calc_perimeter(self):
        return 2 * (self.length + self.length)








