# Delta Lake / Iceberg study guide

This project uses Parquet locally so it stays lightweight. For the lakehouse part, implement the same data model with Delta Lake or Apache Iceberg later.

Study these concepts:
- object storage as durable storage
- table metadata separate from data files
- snapshots / table versions
- ACID commits
- schema evolution
- partition pruning
- compaction / small-file problem
- time travel
- concurrent writers
- Z-ordering / clustering concepts

Mental model:
```text
S3 / object storage
   |
   +-- Parquet data files
   +-- table metadata / snapshots
             |
             v
        Delta / Iceberg table
```
