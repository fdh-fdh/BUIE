class BreakdownExtractor:
    def __init__(self,file):
        self.file = file
        self.breakdown = {"spatialContainer": [], "GUID": [], "nestedContainers": []}

    def get_spatial_breakdown(self):
        Ifc_Project = self.file.by_type("IfcProject")
        self.breakdown["nestedContainers"].append(self.move_level_down(Ifc_Project[0]))

    def move_level_down(self, IfcObjectDefinition):
            container_smaller = {"spatialContainer": "", "GUID":"", "nestedContainers": ""}
            container_smaller["spatialContainer"]=(IfcObjectDefinition.is_a())
            container_smaller["GUID"]=(IfcObjectDefinition.id())
            if hasattr(IfcObjectDefinition, "IsDecomposedBy") and len(IfcObjectDefinition.IsDecomposedBy) != 0:
                decomposed_element= IfcObjectDefinition.IsDecomposedBy[0].RelatedObjects
                if len(decomposed_element) == 0:
                    # container_smaller["spatialContainer"]=IfcObjectDefinition.is_a()
                    # container_smaller["GUID"]= IfcObjectDefinition.id()
                    return container_smaller
                else:
                    for j in decomposed_element:
                        # container_smaller["spatialContainer"]=(j.is_a())
                        # container_smaller["GUID"]=(j.id())
                        container_smaller["nestedContainers"]= self.move_level_down(j)
