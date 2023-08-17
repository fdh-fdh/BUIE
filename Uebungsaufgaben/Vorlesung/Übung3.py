class fahrzeug:
    def __init__(self,geschwindigkeit,maxgeschwindigkeit):
        self.geschwindigkeit = geschwindigkeit
        self.maxgeschwindigkeit = maxgeschwindigkeit
        print('neues Auto!')

    def beschleunige(self, speed):
        a= self.geschwindigkeit + speed
        if a < self.maxgeschwindigkeit:
            self.geschwindigkeit=a
            print(self.geschwindigkeit)
        else:
            print('diese geschwindigkeit kann leider nicht verwirklichen')

    def bremse(self,speed):
        a = self.geschwindigkeit-speed
        if a>0:
            self.geschwindigkeit= a
            print(self.geschwindigkeit)
        else:
            print('diese geschwindigkeit kann leider nicht verwirklichen')

class LKW(fahrzeug):
    def __init__(self,geschwindigkeit,maxgeschwindigkeit,tonnage):
        super().__init__(self, geschwindigkeit, maxgeschwindigkeit)
        self.tonnage = tonnage


class PKW(fahrzeug):
    def __init__(self, geschwindigkeit, maxgeschwindigkeit, sitzplatz):
        super().__init__(self, geschwindigkeit, maxgeschwindigkeit)
        self.sitzplatz = sitzplatz


f1 = fahrzeug(100,200)
f1.beschleunige(20)
f1.beschleunige(200)
f1.bremse(100)

pkw = PKW(100,250,3)
pkw.bremse(50)
pkw.beschleunige(30)