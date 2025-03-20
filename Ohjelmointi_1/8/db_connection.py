import mysql.connector

def get_connection():
    yhteys = mysql.connector.connect(
        host='localhost',
        port=3306,
        database='flight_game',
        user='levk',
        password='mornings-dears-margie',
        collation='utf8mb4_general_ci',
        autocommit=True
    )
    return yhteys