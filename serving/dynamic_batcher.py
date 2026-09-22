import time,random,numpy as np
def model(batch): time.sleep(.005); return np.sum(batch,axis=1)
def naive(xs): return [model(np.asarray([x]))[0] for x in xs]
def batched(xs,k=8):
 out=[]
 for i in range(0,len(xs),k): out.extend(model(np.asarray(xs[i:i+k])).tolist())
 return out
def main():
 xs=[random.random() for _ in range(100)]; t=time.perf_counter(); naive(xs); a=time.perf_counter()-t; t=time.perf_counter(); batched(xs); b=time.perf_counter()-t; print('naive',a,'batched',b,'speedup',a/b)
if __name__=='__main__': main()
