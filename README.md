
## Coverage
- Spark/PySpark: DataFrames, partitions, Catalyst, broadcast joins, skew, salting
- Ray Core: remote tasks, actors, parallel Python, Ray Tune
- Dask: parallel pandas-style computation
- Parquet + PyArrow: columnar storage, pruning, filtering, serialization
- Delta/Iceberg concepts: ACID/object-storage lakehouse patterns
- Kafka/Redpanda: topics, partitions, offsets, consumer groups, at-least-once
- Flink: event time, watermarks, keyed state, windows, backpressure
- dbt, Airflow, Dagster
- PyTorch DDP, FSDP concepts, Accelerate, Ray Tune
- asyncio, Celery/Redis, dynamic batching
- ONNX Runtime and quantization concepts
- vLLM/Triton serving concepts
- latency/throughput, compute vs I/O vs network bottlenecks
- Arrow, skew mitigation, communication/compute overlap

## Install incrementally
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m data.generate
```
Optional stacks:
```bash
pip install -r requirements/spark.txt
pip install -r requirements/dask.txt
pip install -r requirements/ray.txt
pip install -r requirements/streaming.txt
pip install -r requirements/orchestration.txt
pip install -r requirements/distributed_training.txt
pip install -r requirements/serving.txt
```

## Labs
```text
01 Parquet + Arrow
02 Spark
03 Dask
04 Ray Core
05 Spark skew/broadcast/salting
06 Kafka/Redpanda producer+consumer
07 Flink event-time architecture
08 dbt transformations
09 Airflow DAG
10 Dagster assets
11 PyTorch DDP
12 FSDP memory model
13 Accelerate
14 Ray Tune
15 asyncio latency
16 Celery + Redis
17 dynamic batching
18 ONNX Runtime
19 precision/quantization
20 vLLM/Triton serving architecture
```

Start here:
```bash
python -m labs.lab01_parquet_arrow
python -m labs.lab02_spark
python -m labs.lab03_dask
python -m labs.lab04_ray
python -m labs.lab05_spark_skew
```

For streaming:
```bash
docker compose -f infra/docker-compose.streaming.yml up -d
python -m labs.lab06_kafka_producer
python -m labs.lab06_kafka_consumer
```

For distributed training:
```bash
torchrun --standalone --nproc_per_node=2 -m training.ddp_train
python -m training.fsdp_train
accelerate launch training/accelerate_train.py
python -m training.ray_tune
```

For async/serving:
```bash
python -m serving.lab15_async
docker compose -f infra/docker-compose.redis.yml up -d
celery -A serving.celery_app worker --loglevel=INFO
python -m serving.submit_jobs
python -m serving.dynamic_batcher
python -m serving.onnx_demo
```

## Mental models

### Spark
```text
logical query -> Catalyst -> physical plan -> stages -> tasks -> partitions
```

### Ray
```text
Python function -> remote task -> worker
Python class -> remote actor -> stateful worker
```

### Kafka
```text
producer -> topic -> partitions -> consumer group -> offsets
```

### DDP
```text
GPU0 batch0 -> gradients --\
GPU1 batch1 -> gradients --- ALLREDUCE -> synchronized gradients
GPU2 batch2 -> gradients --/
```

### FSDP
```text
DDP: every GPU stores full parameters/gradients/optimizer state
FSDP: those states are sharded; layers gather what they need and reshard
```

### Latency
```text
queue + network + preprocessing + model + postprocessing
```

### Dynamic batching
```text
request1 \ 
request2  ---> batch ---> model
request3 /
```

## Capstone
Build a production-shaped abnormal AE detector:
```text
AE sensors -> Parquet -> Spark batch features
                    \-> Kafka -> Flink streaming features
                                      |
                              feature table
                                      |
                         PyTorch/XGBoost model
                                      |
                                   FastAPI
                              /             \
                         fast path       slow path
                                           Celery/Ray
```
Measure throughput, p50, p95, CPU, memory, GPU utilization and network usage. Then explain the bottleneck rather than only reporting accuracy.

## Geophysics extension
Use magnitude, inter-event time, fault-normal distance z, pressure and event rate to predict whether the next experimental cycle has increasing peak slip velocity. Use time-based splits and explicitly test for leakage.


