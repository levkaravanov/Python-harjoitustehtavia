import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    try:
        connect = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT")),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            collation='utf8mb4_general_ci',
            autocommit=True
        )
        return connect
    except mysql.connector.Error as e:
        print(f"Database connection error: {e}")
        return None