from serving.celery_app import expensive_prediction
def main():
 for i in range(5): print(expensive_prediction.delay(100000+i*1000).id)
if __name__=='__main__': main()
