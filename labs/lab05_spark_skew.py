from pyspark.sql import SparkSession
from pyspark.sql.functions import broadcast,lit,monotonically_increasing_id,pmod

def main():
 s=SparkSession.builder.master('local[*]').appName('Skew').getOrCreate(); e=s.read.parquet('data/generated/ae_events.parquet'); small=s.createDataFrame([('EXP_A','a'),('EXP_B','b'),('EXP_C','c'),('EXP_D','d')],['experiment_id','meta'])
 print('broadcast join'); e.join(broadcast(small),'experiment_id').groupBy('experiment_id').count().show()
 n=16; large=e.withColumn('salt',pmod(monotonically_increasing_id(),lit(n)).cast('int')); salts=s.range(n).withColumnRenamed('id','salt'); small2=small.crossJoin(salts); print('salted join'); large.join(small2,['experiment_id','salt']).groupBy('experiment_id').count().show(); s.stop()
if __name__=='__main__': main()
