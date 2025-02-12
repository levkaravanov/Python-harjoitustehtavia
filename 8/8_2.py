from db_connection import get_connection

yhteys = get_connection()
kursori = yhteys.cursor()

maakoodi = input("Anna maakoodi: ")

sql = ("SELECT type, COUNT(type) "
       "FROM airport "
       "WHERE iso_country = %s "
       "GROUP BY type")
kursori.execute(sql, (maakoodi,))
tulos = kursori.fetchall()

for typpi in tulos:
       print(f"{typpi[0]} - {typpi[1]}")