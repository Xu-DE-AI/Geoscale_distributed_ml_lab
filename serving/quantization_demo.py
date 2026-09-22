import torch
def main():
 for d in [torch.float32,torch.float16,torch.bfloat16,torch.int8]:
  x=torch.empty(10_000_000,dtype=d); print(d,x.numel()*x.element_size()/1024**2,'MB')
if __name__=='__main__': main()
