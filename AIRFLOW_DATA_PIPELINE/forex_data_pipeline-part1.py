from urllib import response
from airflow import DAG
from airflow.providers.http.sensors.http import HttpSensor

from datetime import datetime, timedelta

default_args = {
    "owner":"airflow",
    "email_on_failure":False,
    "email_on_retry":False,
    "email":"admin@gmail.com",
    "retries":1,
    "retry_on_delay":timedelta(minutes=5)
}

##linkAPI
##https://gist.github.com/isbakhul21/eb8f1ced7570c12f30a47cfe255c50da

with DAG("forex_data_pipeline", star_date=datetime(2022,1,1),
    schedule_interval="@daily", default_args=default_args, catchup=False) as dag:

    is_forex_rates_available = HttpSensor(
        task_id = "is_forex_rates_available",
        http_conn_id = "forex_api",
        endpoint="marclamberti/f45f872dea4dfd3eaa015a4a1af4b39b",
        response_check= lambda response:"rates" in response.text,
        poke_interval=5,
        timeout=20
    )
    




