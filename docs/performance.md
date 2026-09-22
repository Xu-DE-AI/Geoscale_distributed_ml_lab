# Performance experiments

For every system record:
- throughput
- p50 latency
- p95 latency
- CPU
- memory
- network
- partition sizes
- GPU utilization

Decompose request latency:
queue + network + preprocessing + model + postprocessing.

Distributed training:
overlap communication with computation where possible.

Spark:
inspect partition sizes and physical plans; test broadcast joins and salting.

Serialization:
compare Python objects with Arrow/Parquet and observe the cost of conversions.
