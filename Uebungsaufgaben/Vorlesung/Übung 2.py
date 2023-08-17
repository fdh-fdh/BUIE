class Rechteck:
    def __init__(self, laenge, breite):
        self.__laenge = laenge
        self.__breite = breite

    @property
    def laenge(self):
        return self.__laenge
    @laenge.setter
    def laenge(self,laenge):
        self.__laenge = laenge

    @property
    def breite(self):
        return self.__breite

    @breite.setter
    def breite(self,breite):
        self.__breite = breite

    def umfang(self):
        return (self.__breite+self.__laenge)*2


rechteck1 = Rechteck(2, 4)
rechteck1.umfang()
