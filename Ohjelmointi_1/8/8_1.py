"""Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin. Ohjelma hakee ja tulostaa koodia vastaavan
lentokentän nimen ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta. ICAO-koodi on tallennettuna
airport-taulun ident-sarakkeeseen."""

from db_connection import get_connection

yhteys = get_connection()
kursori = yhteys.cursor()

koodi = input("Anna ICAO-koodi: ")

sql = "SELECT name, municipality FROM airport WHERE ident = %s"
kursori.execute(sql, (koodi,))

tulos = kursori.fetchone()

if tulos:
    print(f"Lentoasema: {tulos[0]}, Sijaintikunta: {tulos[1]}")
else:
    print("Lentoasemaa ei löytynyt annetulla ICAO-koodilla.")

yhteys.close()