import ermittle_preis as ep

Test_anf_1="A"
Test_anf_2="C"
Test_anf_3="D"
Test_anf_4="F"
Test_anf_5="B"
Test_anf_6="F"

Test_end_1="B"
Test_end_2="I"
Test_end_3="H"
Test_end_4="C"
Test_end_5="E"
Test_end_6="G"

true = 'Ja'
false = 'Nein'
erg1 =ep.ermittle_preis(Test_anf_1,Test_end_1,0)
if erg1 == 8.0:
    print("true")
else:
    print("false")
erg2 =ep.ermittle_preis(Test_anf_2,Test_end_2, 0)
if erg2 == 1.6:
    print("true")
else:
    print("false")
erg3 =ep.ermittle_preis(Test_anf_3,Test_end_3, 1)
print(erg3)
if erg3 == 4.8:
    print("true")
else:
    print("false")
erg4 =ep.ermittle_preis(Test_anf_4,Test_end_4, 1)
print(erg4)
if erg4 == 6.4:
    print("true")
else:
    print("false")
erg5 =ep.ermittle_preis(Test_anf_5,Test_end_5, 1)
if erg5 == 3.2:
    print("true")
else:
    print("false")
erg6= ep.ermittle_preis(Test_anf_6,Test_end_6, 0)
if round(erg6) == 4.8:
    print("true")
else:
    print("false")
