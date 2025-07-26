import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        print(f'{url} → Status: {response.status}')
        return await response.text()

async def main():
    urls = [
        'https://httpbin.org/delay/2',
        'https://httpbin.org/delay/3',
        'https://httpbin.org/delay/1'
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        await asyncio.gather(*tasks)

asyncio.run(main())
