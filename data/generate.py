from pathlib import Path
import numpy as np, pandas as pd
OUT=Path('data/generated'); OUT.mkdir(parents=True,exist_ok=True)
def main():
 rng=np.random.default_rng(42); n=120_000
 ts=pd.date_range('2026-01-01',periods=n,freq='min')
 region=np.where(rng.random(n)<.72,'fault_zone','far_field')
 df=pd.DataFrame({
  'experiment_id':rng.choice(['EXP_A','EXP_B','EXP_C','EXP_D'],n),
  'timestamp':ts,'event_id':np.arange(n),'magnitude':.5+.7*rng.random(n)+.002*np.arange(n)/1000+rng.normal(0,.08,n),
  'dt':np.maximum(.01,rng.lognormal(-1.1,.8,n)),'x':rng.normal(0,20,n),'y':rng.normal(0,20,n),
  'z':np.where(region=='fault_zone',rng.normal(0,3,n),rng.normal(0,15,n)),
  'pressure':5+80*np.linspace(0,1,n)+rng.normal(0,2,n),'temperature':25+rng.normal(0,.5,n),
  'sensor_id':rng.choice([f'S{i:02d}' for i in range(1,17)],n),'region':region})
 sensors=pd.DataFrame({'sensor_id':[f'S{i:02d}' for i in range(1,17)],'sensor_type':['PZT']*16,'sampling_mhz':[10.]*16,'x':rng.normal(0,25,16),'y':rng.normal(0,25,16),'z':rng.normal(0,25,16)})
 experiments=pd.DataFrame({'experiment_id':['EXP_A','EXP_B','EXP_C','EXP_D'],'confining_pressure_mpa':[35,115,115,115],'injection_rate_mpa_min':[2,2,2,8],'rock':['Bentheim sandstone']*4})
 df.to_parquet(OUT/'ae_events.parquet',index=False); df.to_csv(OUT/'events.csv',index=False); sensors.to_parquet(OUT/'sensors.parquet',index=False); experiments.to_parquet(OUT/'experiments.parquet',index=False)
 print(f'Wrote {len(df):,} events')
if __name__=='__main__': main()
