import asyncio


async def send_one() -> None:
    n: int = 0
    while True:
        await asyncio.sleep(1)
        n += 1
        if n % 3 != 0:

            print(f"Dastur ishga tushganiga {n} soniya bo'ldi.")


async def send_three() -> None:
    n: int = 0
    while True:
        await asyncio.sleep(3)
        n += 3
        print(f"Dastur ishga tushganiga {n} soniya bo'ldi.")


async def main() -> None:
    task_1 = asyncio.tasks.create_task(send_one())
    task_3 = asyncio.tasks.create_task(send_three())
    await task_1, task_3
    # await task_3


if __name__ == "__main__":
    asyncio.run(main())
