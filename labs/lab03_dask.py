import dask.dataframe as dd
def main():
 df=dd.read_parquet('data/generated/ae_events.parquet'); print('partitions',df.npartitions); print(df[df.magnitude>1].groupby('experiment_id').magnitude.mean().compute())
if __name__=='__main__': main()
