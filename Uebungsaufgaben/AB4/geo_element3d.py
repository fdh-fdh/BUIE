from abc import abstractmethod
import AF4 as AF4


class geo_element3d(AF4.geo_element):
    @abstractmethod
    def calc_volume(self):
        pass

