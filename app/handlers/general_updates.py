from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.enums import ParseMode

router = Router()


@router.message(Command('start'))
async def start_cmd(message: Message):
    await message.answer(f"Welcome, <b>{message.from_user.first_name}</b>\n"
                         f"You can ask me about Java releases. Just type '/java_releases'.\n\n"
                         f"P.S. In the future, I wil have more functionality :)", parse_mode=ParseMode.HTML)
