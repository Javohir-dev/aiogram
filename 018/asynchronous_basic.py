import asyncio


async def send_time(sec: int) -> None:
    while True:
        await asyncio.sleep(sec)
        print(f"Sec: {sec}")


# print(send_time(2), send_time(5), sep="\n")


async def main() -> None:
    task_1 = asyncio.create_task(send_time(2))
    task_2 = asyncio.create_task(send_time(5))
    await task_1
    await task_2


if __name__ == "__main__":
    asyncio.run(main())
