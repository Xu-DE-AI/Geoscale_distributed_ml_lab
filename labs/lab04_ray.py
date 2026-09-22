import ray, numpy as np, time

def score(e,seed):
 x=np.random.default_rng(seed).normal(size=2_000_000); return e,float(np.mean(np.sin(x)**2))
@ray.remote
def score_remote(e,seed): return score(e,seed)
@ray.remote
class Counter:
 def __init__(self): self.n=0
 def run(self,e,seed): self.n+=1; return {'result':score(e,seed),'calls':self.n}
def main():
 ex=list(zip(['EXP_A','EXP_B','EXP_C','EXP_D'],range(4))); t=time.perf_counter(); print([score(*x) for x in ex]); print('seq',time.perf_counter()-t); ray.init(ignore_reinit_error=True,include_dashboard=False); t=time.perf_counter(); print(ray.get([score_remote.remote(*x) for x in ex])); print('ray',time.perf_counter()-t); c=Counter.remote(); print(ray.get([c.run.remote(*x) for x in ex])); ray.shutdown()
if __name__=='__main__': main()
