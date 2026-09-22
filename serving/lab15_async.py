import asyncio,time
async def call(i): await asyncio.sleep(.1); return i
async def main():
 t=time.perf_counter(); await asyncio.gather(*(call(i) for i in range(20))); print('20 concurrent I/O calls:',time.perf_counter()-t)
if __name__=='__main__': asyncio.run(main())
