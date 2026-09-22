import torch
from torch import nn
from torch.utils.data import DataLoader,TensorDataset
from accelerate import Accelerator
def main():
 a=Accelerator(); x=torch.randn(10000,16); y=(x[:,0]+x[:,1]>0).long(); dl=DataLoader(TensorDataset(x,y),batch_size=128,shuffle=True); m=nn.Sequential(nn.Linear(16,32),nn.ReLU(),nn.Linear(32,2)); o=torch.optim.AdamW(m.parameters(),1e-3); m,o,dl=a.prepare(m,o,dl)
 for ep in range(2):
  for xb,yb in dl: o.zero_grad(); loss=nn.functional.cross_entropy(m(xb),yb); a.backward(loss); o.step()
  a.print('epoch',ep,'loss',loss.item())
if __name__=='__main__': main()
