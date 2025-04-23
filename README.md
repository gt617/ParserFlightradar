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

## Файл make_report.py:

Создает таблицу hourly_report с отчетом о колчичестве рейсов за последний час (по параметрам airline и model).

Структура таблицы:

- airline - название авиакомпании (varchar)
- model - модель самолета (varchar)
- count - кол-во рейсов данной модели и данной авиакампании за последний час (varchar)

## Пример файла .env:

```
POSTGRES_PASSWORD=your_pswd
POSTGRES_DB=your_db
POSTGRES_USER=your_user
PGUSER=your_user
DB_HOST=db
DB_PORT=5432
```

## Запуск проекта:
Загрузите проект на свой локальный репозиторий и в дериктории ParserFlightradar/ выполните
```
docker compose up -d
```
Просмотр таблиц:
```
docker compose exec -it db psql
>>>\dt
>>>SELECT * FROM <название таблицы>;
```
