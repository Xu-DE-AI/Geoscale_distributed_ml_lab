from pyspark.sql import SparkSession
from pyspark.sql.functions import avg,count,broadcast
def main():
 s=SparkSession.builder.master('local[*]').appName('GeoScaleSpark').config('spark.sql.adaptive.enabled','true').getOrCreate(); e=s.read.parquet('data/generated/ae_events.parquet'); sensors=s.read.parquet('data/generated/sensors.parquet')
 print('rows',e.count(),'partitions',e.rdd.getNumPartitions())
 e.groupBy('experiment_id','region').agg(count('*').alias('n'),avg('magnitude').alias('mean_mag')).show()
 j=e.join(broadcast(sensors),'sensor_id','left'); j.explain('formatted'); print('joined',j.count()); s.stop()
if __name__=='__main__': main()
