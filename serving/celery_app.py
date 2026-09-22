from celery import Celery
app=Celery('geoscale',broker='redis://localhost:6379/0',backend='redis://localhost:6379/1')
@app.task
def expensive_prediction(x): return sum(i*i for i in range(x))
