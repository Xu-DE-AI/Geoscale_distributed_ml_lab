import torch
import torch.distributed as dist
from torch import nn
from torch.utils.data import DataLoader,TensorDataset,DistributedSampler

def main():
 dist.init_process_group('gloo'); rank=dist.get_rank(); x=torch.randn(20000,16); y=(x[:,0]+.5*x[:,1]>0).long(); ds=TensorDataset(x,y); sam=DistributedSampler(ds); dl=DataLoader(ds,batch_size=128,sampler=sam); model=nn.Sequential(nn.Linear(16,32),nn.ReLU(),nn.Linear(32,2)); model=nn.parallel.DistributedDataParallel(model); opt=torch.optim.AdamW(model.parameters(),1e-3)
 for ep in range(3):
  sam.set_epoch(ep); total=0
  for xb,yb in dl: opt.zero_grad(); loss=nn.functional.cross_entropy(model(xb),yb); loss.backward(); opt.step(); total+=loss.item()
  if rank==0: print(ep,total/len(dl))
 dist.destroy_process_group()
if __name__=='__main__': main()
