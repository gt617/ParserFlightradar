FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

CMD python data2db.py FIRST COMMAND; python make_report.py SECOND COMMAND