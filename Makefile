data:
	python -m data.generate
spark:
	python -m labs.lab02_spark
dask:
	python -m labs.lab03_dask
ray:
	python -m labs.lab04_ray
skew:
	python -m labs.lab05_spark_skew
ddp:
	torchrun --standalone --nproc_per_node=2 -m training.ddp_train
async:
	python -m serving.lab15_async
batch:
	python -m serving.dynamic_batcher
