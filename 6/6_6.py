"""Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä
sekä pizzan hinnan euroina. Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa
paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta). Yksikköhintojen laskennassa on
hyödynnettävä kirjoitettua funktiota."""

import math

def yksikkohinta(halkaisija, hinta):
    sade = halkaisija / 2
    pinta_ala = math.pi * sade ** 2
    hinta_per_m2 = hinta / pinta_ala
    return hinta_per_m2

halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija (cm): "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta (€): "))
halkaisija2 = float(input("Anna toisen pizzan halkaisija (cm): "))
hinta2 = float(input("Anna toisen pizzan hinta (€): "))

if yksikkohinta(halkaisija1, hinta1) < yksikkohinta(halkaisija2, hinta2):
    print("Ensimmäinen pizza on edullisempi.")
elif yksikkohinta(halkaisija1, hinta1) > yksikkohinta(halkaisija2, hinta2):
    print("Toinen pizza on edullisempi.")
else:
    print("Molemmat pizzat ovat sama")