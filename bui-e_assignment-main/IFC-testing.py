import ifcopenshell

model = ifcopenshell.open("00_SampleModels/Brueckenueberbau_types.ifc")

print(model.schema)

beams = model.by_type("IfcProject")

for beam in beams:

    print(beam.Name)



