import json
from confluent_kafka import Consumer
def main():
 c=Consumer({'bootstrap.servers':'localhost:19092','group.id':'geoscale-lab','auto.offset.reset':'earliest','enable.auto.commit':False}); c.subscribe(['ae-events'])
 try:
  while True:
   m=c.poll(1)
   if m is None: continue
   if m.error(): print(m.error()); continue
   e=json.loads(m.value()); print('event',e['event_id'],'partition',m.partition(),'offset',m.offset()); c.commit(message=m,asynchronous=False)
 except KeyboardInterrupt: pass
 finally: c.close()
if __name__=='__main__': main()
