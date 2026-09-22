from pathlib import Path
import time, pandas as pd
import pyarrow.dataset as ds

def main():
 if not Path('data/generated/ae_events.parquet').exists(): from data.generate import main as g; g()
 p='data/generated/ae_events.parquet'; t=time.perf_counter(); pd.read_parquet(p,columns=['timestamp','magnitude','z']); print('Pandas:',time.perf_counter()-t)
 d=ds.dataset(p,format='parquet'); t=time.perf_counter(); tab=d.to_table(columns=['timestamp','magnitude','z'],filter=ds.field('magnitude')>1.0); print('Arrow filtered:',time.perf_counter()-t,'rows=',tab.num_rows)
if __name__=='__main__': main()
