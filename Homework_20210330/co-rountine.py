
import asyncio
import time
import csv
async def readfile(q):
    # TODO
    file=open("IBM_2006-01-01_to_2018-01-01.csv")
    for i,line in enumerate(file):
        if(i%2==0):
            continue
        else:
            await q.put(line)
    await q.put(None)
    await q.join()

async def writefile(q):
    # TODO
    file=open("new.csv","w")
    while True:
        item=await q.get()
        if item is None:
            q.task_done()
            break
        else:
            file.write(item)
            q.task_done()
    
    
async def main():
    print(f"start at {time.strftime('%X')}")
    # TODO
    q=asyncio.Queue()
    loop=asyncio.get_event_loop()
    tasks=[readfile(q),writefile(q)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    print(f"finish at {time.strftime('%X')}")

asyncio.run(main())
