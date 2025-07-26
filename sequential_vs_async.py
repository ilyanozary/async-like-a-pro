import asyncio
import time

def sync_task():
    print("[sync] Start")
    time.sleep(2)
    print("[sync] End")

async def async_task():
    print("[async] Start")
    await asyncio.sleep(2)
    print("[async] End")

async def main():
    print("Running sync:")
    sync_task()
    sync_task()

    print("\nRunning async:")
    await asyncio.gather(async_task(), async_task())

asyncio.run(main())
