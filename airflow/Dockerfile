FROM apache/airflow:2.9.0

ENV PYTHONPATH "${PYTHONPATH}:/usr/local/airflow/scripts"
ENV AIRFLOW__CORE__LOAD_EXAMPLES=True
ENV AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=my_conn_string
COPY requirements.txt /
RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" -r /requirements.txt
