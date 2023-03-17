import asyncio
import telegram

TOKEN = ""


async def main():
    bot = telegram.Bot(token=TOKEN)
    print(await bot.get_me())


if __name__ == '__main__':
    asyncio.run(main())
