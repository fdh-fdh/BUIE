import xml.dom.minidom


class Person:
    def __init__(self,name, vorname):
        self.name = name
        self.vorname = vorname


doc = xml.dom.minidom.parse("personen.xml")

person_list = []

for personnode in doc.getElementsByTagName("Person"):
    name = personnode.getElementsByTagName("name")[0].firstChild.data
    vorname = personnode.getElementsByTagName("vorname")[0].firstChild.data
    print("new person: ", name, vorname)
    person = Person(name,vorname)
    person_list.append(person)




