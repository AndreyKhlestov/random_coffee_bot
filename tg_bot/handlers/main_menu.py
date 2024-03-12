from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from tg_bot.middlewares.blocking import BlockingMiddleware
from tg_bot.keyboards.reply import kb_main_menu


main_router = Router()
main_router.message.middleware(BlockingMiddleware())
main_router.callback_query.middleware(BlockingMiddleware())


@main_router.message(Command('start'))
async def main_menu(message: Message):
    """Ввод команды /start"""
    await message.answer(
        'Что умеет этот бот?'
        '\n☕️Мы продолжаем нашу прекрасную традицию знакомиться за чашечкой '
        'горячего кофе или чая.'
        '\n🗓️ С кем ты разделишь капучино - решает случай. Каждый понедельник '
        'в этом боте будет происходить рассылка с именем коллеги, '
        'с кем вам нужно организовать встречу.'
        '\n🔁Участники выбираются случайным образом, поэтому вы сможете выпить '
        'кофе с теми, с кем еще не пересекались по работе.'
        '\nДобро пожаловать🥰',
        reply_markup=kb_main_menu())
