import asyncio

async def greet(name):
    print(f"Hello, {name}!")
    # await asyncio.sleep(1)
    print("Goodbye!")

async def main():
    await greet("Bob")
    greet("Alice")

asyncio.run(main())
