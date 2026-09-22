from pathlib import Path
import pandas as pd
def test_schema():
 p=Path('data/generated/ae_events.parquet')
 if not p.exists(): return
 df=pd.read_parquet(p); assert {'event_id','experiment_id','timestamp','magnitude','dt','x','y','z'}.issubset(df.columns)
