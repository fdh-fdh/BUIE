def preis_von_bis(zone_ab, zone_bis):
    if zone_ab < zone_bis:
        zone_klein = zone_ab
        zone_gross = zone_bis
    else:
        zone_klein = zone_bis
        zone_gross = zone_ab

    preis = 1.6 * (zone_gross - zone_klein + 1)
    return preis


#Beispiel falls man von 6 zur 4 fahren dann ist 6-4= 2, aber ist insgesamt 4,5,6 :
   # 3 zone.)