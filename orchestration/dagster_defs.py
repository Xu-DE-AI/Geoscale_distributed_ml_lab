from pathlib import Path
from dagster import Definitions,asset
@asset
def raw_events(): return Path('data/generated/ae_events.parquet').exists()
@asset
def validate_events(raw_events): return raw_events
defs=Definitions(assets=[raw_events,validate_events])
