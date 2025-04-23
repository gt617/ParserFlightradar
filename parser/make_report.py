import psycopg2
import os
from datetime import datetime as dt, timedelta

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
            """CREATE TABLE IF NOT EXISTS hourly_report (
                airline VARCHAR(50) NOT NULL,
                model VARCHAR(50) NOT NULL,
                count VARCHAR(3) NOT NULL);"""
        )
        prev_hour = (dt.now() - timedelta(hours=1)).time()
        cursor.execute(f"""SELECT airline, model, COUNT(model)
                        FROM flights WHERE record_time >= '{prev_hour}'
                        GROUP BY  airline, model;""")
        flights = cursor.fetchall()
        cursor.executemany("""
                INSERT INTO hourly_report (airline, model, count)
                VALUES (%s, %s, %s)
                """, flights)

except Exception as ex:
    print("[INFO] Error while connection", ex)

finally:
    if connection:
        connection.commit()
        connection.close()
        print("[INFO] PostgreSQL connetion closed")
