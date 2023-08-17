import ermittle_zone as ez
import preis_von_bis as pvb


def ermittle_preis(halt_anf, halt_end, durch):
    zone_anf= ez.ermittle_zone(halt_anf)
    zone_end= ez.ermittle_zone(halt_end)
    if durch == 0:
        preis = pvb.preis_von_bis(zone_anf, zone_end)
    else:
        if durch == 1:
            teil1 = pvb.preis_von_bis(zone_anf, 1)
            teil2 = pvb.preis_von_bis(1, zone_end)
            preis = teil1 + teil2 - 1.6

    return preis

