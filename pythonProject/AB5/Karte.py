#Element Karte werden Hier implementiert


class Card:
    def __init__(self, color: str, number: int):
        # self._id = id_number
        self.color = color
        self.number = number

    def __repr__(self):
        print("Presenting your card: Number is "+ str(self.number) + ", Color is " + self.color)





"""
    def get_color(self):
        return self._color

    def get_id(self):
        return self._id

    def get_number(self):
        return self._number

    def set_color(self, color):
        while True:
            try:
                self._color = color
            except TypeError:
                print("Wrong Type: color should be type str")
            else:
                return

    def set_number(self,number):
        while True:
            try:
                self._number = number
            except TypeError:
                print("Wrong Type: number should be type integer")
            else:
                return
"""