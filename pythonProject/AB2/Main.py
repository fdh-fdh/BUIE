import ermittle_preis as ep

halt_anf = str(input('Geben Sie die Anfanghaltestelle: '))
halt_end = str(input('Geben Sie die Endhaltestelle: '))
durch = str(input('umsteigen? : (0),(1)'))
Preis = ep.ermittle_preis(halt_anf, halt_end, durch)
print(Preis)






