import math as mt

class kreis:

    def __init__(self, radius):
        self.radius = radius

    def umfang(self):
        a = mt.pi*self.radius*self.radius
        return a
    
    def __del__(self):
        print('KREIS GELÖSCHT')

a = kreis(2)
print(a.umfang())
del a





