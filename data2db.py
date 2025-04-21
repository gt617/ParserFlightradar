import psycopg2

from config import host, user, password, db_name
from my_parser import get_flights_information


try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS flights (
                record_time VARCHAR(50) NOT NULL,
                collsing VARCHAR(10) NOT NULL,
                icao VARCHAR(5) NOT NULL,
                model VARCHAR(50) NOT NULL,
                airline VARCHAR(50) NOT NULL,
                origin_airport VARCHAR(5) NOT NULL,
                destination_airport VARCHAR(5) NOT NULL,
                latitude FLOAT NOT NULL,
                longitude FLOAT NOT NULL);
            """
        )
        cursor.executemany("""
                INSERT INTO flights (record_time, collsing,
                                     icao, model, airline,
                                     origin_airport, destination_airport,
                                     latitude, longitude)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, get_flights_information())

except Exception as ex:
    print("[INFO] Error while connection", ex)

finally:
    if connection:
        connection.commit()
        connection.close()
        print("[INFO] PostgreSQL connetion closed")
