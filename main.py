import asyncio
from time import time

async def foo():
    print('[foo] Step one')
    await asyncio.sleep(3)
    print('[foo] Step two')

async def bar():
    print('[bar] Starting...')
    for i in range(3):
        await asyncio.sleep(1)
        print(f'[bar] Working... {i+1}')
    print('[bar] Done')

async def another():
    print('[another] Called right away')

async def main():
    start = time()
    await asyncio.gather(foo(), bar(), another())
    end = time()
    print(f'Finished all in {end - start:.2f} seconds')

asyncio.run(main())
