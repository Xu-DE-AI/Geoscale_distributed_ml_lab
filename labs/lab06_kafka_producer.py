import json,time
from confluent_kafka import Producer
def main():
 p=Producer({'bootstrap.servers':'localhost:19092'})
 for i in range(20):
  e={'event_id':i,'sensor_id':f'S{i%4+1:02d}','magnitude':.5+i*.03,'timestamp':time.time()}; p.produce('ae-events',key=e['sensor_id'],value=json.dumps(e)); p.poll(0); time.sleep(.1)
 p.flush()
if __name__=='__main__': main()
