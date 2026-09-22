def main():
 print('FSDP mental model: DDP stores a full model/gradients/optimizer state on every worker. FSDP shards these states. Layers all-gather parameter shards when needed, compute, then reshard. Study all-gather, reduce-scatter, parameter/gradient/optimizer sharding and activation checkpointing.')
if __name__=='__main__': main()
