import psycopg2
from datetime import datetime as dt, timedelta

from config import host, user, password, db_name

file = open('report.txt', 'w')

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

    with connection.cursor() as cursor:
        airline, model = '', ''
        print('Enter airline: ')
        airline = input()
        print('Enter model: ')
        model = input()
        prev_hour = (dt.now() - timedelta(hours=1)).time()
        print(prev_hour)
        cursor.execute(
            f"SELECT COUNT(*) FROM flights WHERE airline='{airline}' "
            f"AND model='{model}' AND record_time >= '{prev_hour}';")
        count = cursor.fetchone()
        file.write(f"Count of flights in the last hour with "
                   f"parametrs(airline='{airline}', model='{model}'): "
                   f"{count[0]}")

except Exception as ex:
    print("[INFO] Error while connection", ex)

finally:
    if connection:
        connection.commit()
        connection.close()
        file.close()
        print("[INFO] PostgreSQL connetion closed")
