import asyncio
import random

queue = asyncio.Queue()

async def producer():
    for i in range(5):
        await asyncio.sleep(random.uniform(0.5, 1.5))
        item = f"item-{i}"
        await queue.put(item)
        print(f"Produced: {item}")

async def consumer():
    while True:
        item = await queue.get()
        print(f"Consumed: {item}")
        queue.task_done()

async def main():
    consumer_task = asyncio.create_task(consumer())
    await producer()
    await queue.join()
    consumer_task.cancel()

asyncio.run(main())
