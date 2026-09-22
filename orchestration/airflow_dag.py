from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
with DAG('geoscale_pipeline',start_date=datetime(2026,1,1),schedule='@daily',catchup=False) as dag:
 generate=BashOperator(task_id='generate',bash_command='python -m data.generate')
 validate=BashOperator(task_id='validate',bash_command='python -m labs.lab01_parquet_arrow')
 train=BashOperator(task_id='train',bash_command='python -m training.ddp_train')
 generate >> validate >> train
