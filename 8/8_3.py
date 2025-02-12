"""Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit. Ohjelma ilmoittaa lentokenttien välisen
etäisyyden kilometreinä. Laskenta perustuu tietokannasta haettuihin koordinaatteihin. Laske etäisyys geopy-kirjaston
avulla: https://geopy.readthedocs.io/en/stable/. Asenna kirjasto valitsemalla View / Tool Windows / Python Packages.
Kirjoita hakukenttään geopy ja vie asennus loppuun."""

from db_connection import get_connection
from geopy import distance

# Yhteyden muodostaminen tietokantaan
yhteys = get_connection()
kursori = yhteys.cursor()

print("Ohjelma laskee etäisyyden kahden lentokentän välillä.")
ensimmainen_icao = input("Anna 1. lentoaseman ICAO-koodi: ")
toinen_icao = input("Anna 2. lentoaseman ICAO-koodi: ")

# SQL-kysely koordinaattien hakemiseksi
sql = ("SELECT latitude_deg, longitude_deg FROM airport WHERE ident IN (%s, %s)")

kursori.execute(sql, (ensimmainen_icao, toinen_icao))
koordinaatit = kursori.fetchall()

# Tarkistetaan, löytyivätkö molemmat lentoasemat
if len(koordinaatit) < 2:
    print("Virhe: Ainakin yksi lentoasema ei löytynyt.")
else:
    ensimmainen_sijainti = koordinaatit[0]
    toinen_sijainti = koordinaatit[1]

    etaisyys = distance.distance(ensimmainen_sijainti, toinen_sijainti).kilometers
    print(f"Lentoasemien välinen etäisyys: {etaisyys:.2f} km")

# Suljetaan yhteys tietokantaan
yhteys.close()
