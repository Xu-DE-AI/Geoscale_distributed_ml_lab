def main():
 print('Flink exercise: Kafka -> timestamps/watermarks -> key_by(sensor_id) -> 1-minute event-time window -> aggregate -> sink. Study event time vs processing time, late events, state, checkpoints and backpressure.')
if __name__=='__main__': main()
