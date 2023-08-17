from abc import ABC, abstractmethod
import math as mt


class Querprofil(ABC):
    @abstractmethod
    def flaechentragheitsmoment(self):
        pass


class RechteckProfil(Querprofil):
    def __init__(self,h,b):
        self.a = h
        self.b = b

    def flaechentragheitsmoment(self):
        return self.b * self.a ** 3 / 12


class kreisProfil(Querprofil):
    def __init__(self, d):
        self.d = d

    def flaechentragheitsmoment(self):
        return mt.pi * self.d ** 4 / 64


a = kreisProfil(5)
b = a.flaechentragheitsmoment()

c = RechteckProfil(2,5)
d = c.flaechentragheitsmoment()
profile = (a,c)

print(b,'      ',d)









