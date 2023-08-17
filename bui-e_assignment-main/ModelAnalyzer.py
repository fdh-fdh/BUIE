import ifcopenshell as ifc
import ifcopenshell.util.element

class ModelAnalyzer:
    def __init__(self, file):
        self.file= file

    def get_instances_by_entity_name(self,entity_name: str, include_subtypes:bool= "false"):
        ins= self.file.by_type(entity_name,include_subtypes)
        instanzen= []
        for i in ins:
            instanzen.append(i)
        return instanzen

    def get_instances_by_type_name(self,type_name:str):

        instanzen = []
        a = self.file.schema
        if a == "IFC2X3":
            return instanzen

        instanzen=self.file.by_type(type_name)
        IfcTypeObjects = []
        for i in instanzen:
            a = i.Types[0].RelatedObjects
            if i.is_a() == "IfcBuildingElement":
                IfcTypeObjects.append(i.Name)
        return IfcTypeObjects

    def count_products(self,typename:str):
        element = {"type":[],"Quantity" :[]}
        for p in self.file.by_type(typename):
            elements = ifc.util.element.get_decomposition(p)
            if len(elements) != 0:
                name = elements[0].is_a()
                try:
                    element["type"].index(name)
                except ValueError:
                    element["type"].append(name)
                    element["Quantity"].append(len(elements))
                else:
                    a = element["type"].index(name)
                    element["Quantity"][a] += len(elements)
        return element

    def count_all_entities(self):
        entity = {"Name":[],"Length":[]}
        for ele in self.file.by_type("IfcRoot"):
            elements = ifc.util.element.get_decomposition(ele)
            if len(elements) != 0:
                entity["Name"].append(ele.Name)
                entity["Length"].append(len(elements))
        return entity

    def get_space_data(self):

        spaces = self.file.by_type("IfcSpace")
        psets={"SpaceCategory":[],"SpaceLevel":[],"SpaceArea":[],"SpaceVolume":[],"SpaceHeight":[]}
        p=[]
        for s in spaces:
            pset = ifc.util.element.get_psets(s)
            psets["SpaceLevel"].append(pset["PSet_Revit_Constraints"]["Level"])
            psets["SpaceCategory"].append(pset["PSet_Revit_Identity Data"]["Name"])
            psets["SpaceArea"].append(pset["PSet_Revit_Dimensions"]["Area"])
            psets["SpaceVolume"].append(pset["PSet_Revit_Dimensions"]["Volume"])
            psets["SpaceHeight"].append(pset["PSet_Revit_Dimensions"]["Unbounded Height"])
            p.append(pset)
        return p,psets
































