# Capstone

Build an abnormal AE detector.

1. Generate 120k events.
2. Store Parquet.
3. Spark batch features.
4. Kafka event stream.
5. Flink event-time rolling features.
6. Train a time-split XGBoost/PyTorch classifier.
7. Serve with FastAPI.
8. Async I/O for telemetry calls.
9. Celery/Ray for slow work.
10. Dynamic batching for model calls.
11. Measure p50/p95 and throughput.

Use geophysical features: magnitude, dt, z, pressure, event rate. Target: whether next experimental cycle has increasing peak slip velocity. Explicitly test temporal leakage.

Report architecture tradeoffs, not only model accuracy.
