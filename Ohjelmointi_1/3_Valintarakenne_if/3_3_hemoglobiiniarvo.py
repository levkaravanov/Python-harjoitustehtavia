sukupuoli = input("Syötä sukupuoli (nainen/mies):").lower()
if sukupuoli == "nainen" or sukupuoli == "mies":
    hemoglobiiniarvo = float(input("Syötä hemoglobiiniarvo (g/l):"))

    alhainen = "Hemoglobiiniarvo on alhainen."
    korkea = "Hemoglobiiniarvo on korkea."
    normaali = "Hemoglobiiniarvo on normaali."

    if sukupuoli == "nainen":
        if hemoglobiiniarvo < 117:
            print(alhainen)
        elif hemoglobiiniarvo > 175:
            print(korkea)
        else:
            print(normaali)
    else:
        if hemoglobiiniarvo < 134:
            print(alhainen)
        elif hemoglobiiniarvo > 195:
            print(korkea)
        else:
            print(normaali)
else:
    print("Virheellinen sukupuoli. Anna sukupuoli muodossa ‘nainen’ tai ‘mies’.")