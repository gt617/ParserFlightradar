import psycopg2
import os

from my_parser import get_flights_information


try:
    connection = psycopg2.connect(
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
        database=os.getenv('POSTGRES_DB'),
        port=os.getenv('DB_PORT'),
        host=os.getenv('DB_HOST')
    )

    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS flights (
                record_time TIME NOT NULL,
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
