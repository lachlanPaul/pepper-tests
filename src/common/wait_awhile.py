"""
    Custom async function to wait for a determined number of seconds

    This is so we can count down asynchronously without making a new function every single time

    Lachlan Paul, 2023
"""
import asyncio

seconds = 5


def main(seconds):
    asyncio.sleep(seconds)
    print("sup")


asyncio.run(main())