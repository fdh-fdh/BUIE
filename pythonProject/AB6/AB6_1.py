import json


class Rectangle:
    def __init__(self,breite, hohe):
        self.breite = breite
        self.hohe = hohe


class Kreis:
    def __init__(self,Durchmesser,Farbe,clockwise):
        self.Durchmesser = Durchmesser
        # self.eigenschaften = Eigenschaften
        self.farbe = Farbe
        self.clockwise = clockwise


class Dreieck:
    def __init__(self,basis,hohe):
        # self.eingenschaften = Eigenschaften
        self.basis = basis
        self.hohe = hohe


with open('2D_Geometrie.json', 'r') as f:
    # read the data
    geo = json.load(f)

relevante_data = geo[" data "]
# print(relevante_data)
# print(type(relevante_data))
rechteck_list = []
for i in relevante_data:
    if i[" Typ "] == " Rechteck ":
        eigenschaftDic = i[" Eigenschaften "]
        R = Rectangle(eigenschaftDic[" Breite "],eigenschaftDic[" Hoehe "])
        rechteck_list.append(R)
        print("Rechteck mit eigenschaft gefunden: " +"Breite "+ str(R.breite )+ " , Hoehe: " + str(R.hohe))
    if i[" Typ "] == " Kreis ":
        eigenschaftDic = i[" Eigenschaften "]
        R = Kreis(eigenschaftDic[" Durchmesser "] , eigenschaftDic[" Farbe "], eigenschaftDic[" Clockwise "])
        rechteck_list.append(R)
        print("Kreis mit eigenschaft gefunden: " +"Breite "+ str(R.Durchmesser )+ " , Hoehe: " + R.farbe+ "Clockwise: " + str(R.clockwise))

    if i[" Typ "] == " Dreieck ":
        eigenschaftDic = i[" Eigenschaften "]
        R = Dreieck(eigenschaftDic[" Basis "], eigenschaftDic[" Hoehe "])
        rechteck_list.append(R)
        print("Dreieck mit eigenschaft gefunden:  " + "Breite " + str(
            R.basis) + " , Hoehe: " + str(R.hohe) )
