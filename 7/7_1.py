talvi = {
    12: "Joulu",
    1: "Tammi",
    2: "Helmi"
}

kevat = {
    3: "Maalis",
    4: "Huhti",
    5: "Touko"
}

kesa = {
    6: "Kesä",
    7: "Heinä",
    8: "Elo"
}

syksy = {
    9: "Syys",
    10: "Loka",
    11: "Marras"
}

kuu = int(input("Anna kuun numero: "))

if kuu in talvi:
    print(f"{talvi[kuu]}kuu on talvessa")
elif kuu in kevat:
    print(f"{kevat[kuu]}kuu on keväässä")
elif kuu in kesa:
    print(f"{kesa[kuu]}kuu on kesässä")
elif kuu in syksy:
    print(f"{syksy[kuu]}kuu on syksyssä")
else:
    print("Virheellinen kuukausinumero!")