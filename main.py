import asyncio
import logging
from datetime import datetime

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

from app.settings import get_bot_config
from app.handlers.general_updates import router as general_updates_router
from app.handlers.java_updates import router as java_updates_router


def custom_commands():
    return [
        BotCommand(command="start", description="Start communication with a bot"),
        BotCommand(command="java_releases", description="Show releases info about all versions data")
    ]


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    dp = Dispatcher()
    dp["started_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")

    bot = Bot(get_bot_config().token)

    dp.include_routers(general_updates_router, java_updates_router)

    await bot.set_my_commands(custom_commands())
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
