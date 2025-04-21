# ParserFlightradar

Проект предоставляет инструменты для парсинга данных с сервиса Flightradar24, включая информацию о рейсах, авиакомпаниях, аэропортах и тд.

## Задача

Написать сервис/скрипт, который загружает данные с FlightRadar24. Для мониторинга возьми акваторию Чёрного моря. Загруженные данные по рейсам должны обязательно содержать позывной, код ICAO, модель самолёта, принадлежность к авиакомпании, а также маршрутные данные, позволяющие рассчитать маршрут полёта.

## Структура таблицы flights из файла data2db.py:

- record_time - время на момент записи (varchar)
- collsing - позывной самолета (varchar)
- icao - код ICAO самолета (varchar)
- model - модель самолета (varchar)
- airline - название авиакомпании (varchar)
- origin_airport - код ICAO аэропорта отбытия (varchar)
- destination_airport - код ICAO аэропорта прибытия (varchar)
- latitude - широта на момент записи (float)
- longitude - долгота на момент записи (float)

Установка зависимостей:```pip install -r requirements.txt```
Запуск сбора данных: ```python data2db.py```

## Файл make_report.py:

Создает отчет о колчичестве рейсов за последний час (по параметрам airline и model).

## Пример файла config.py:

```
host = 'localhost'
user = 'your_user'
password = 'your_password'
db_name = 'your_db'
```

