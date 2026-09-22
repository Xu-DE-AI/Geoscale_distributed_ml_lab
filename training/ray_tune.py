import ray
from ray import tune
from ray.air import session
def train(config):
 score=1/(1+abs(config['lr']-.001)*1000)+config['hidden']/1000; session.report({'score':score})
def main():
 ray.init(ignore_reinit_error=True,include_dashboard=False); t=tune.Tuner(train,param_space={'lr':tune.loguniform(1e-4,1e-2),'hidden':tune.choice([16,32,64,128])},tune_config=tune.TuneConfig(num_samples=8)); r=t.fit(); print(r.get_best_result(metric='score',mode='max').config); ray.shutdown()
if __name__=='__main__': main()
