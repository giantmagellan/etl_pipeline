FROM quay.io/astronomer/astro-runtime:7.3.0
FROM apache/airflow:2.5.1
COPY requirements.txt /requirements.txt
RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir --user -r /requirements.txt