import asyncio, aiohttp


async def create_post(session, title, body):

    async with session.post(
        "https://jsonplaceholder.typicode.com/posts",
        json={"title": title, "body": body, "userId": 1},
    ) as response:
        response.raise_for_status()
        data = await response.json()
        return data


async def main():
    async with aiohttp.ClientSession() as session:
        result = await create_post(session, "My First Post", "Learning Python")
        print(result)


asyncio.run(main())
