from aiogram import Router, F
from aiogram.types import Message

from tg_bot.middlewares.blocking import BlockingMiddleware
from tg_bot.keyboards.reply import kb_main_menu


main_menu_router = Router()
main_menu_router.message.middleware(BlockingMiddleware())
main_menu_router.callback_query.middleware(BlockingMiddleware())


GREETING_TEXT = (
    'Что умеет этот бот?\n'
    '☕️Мы продолжаем нашу прекрасную традицию знакомиться за чашечкой '
    'горячего кофе или чая.\n'
    '🗓️ С кем ты разделишь капучино - решает случай. Каждый понедельник '
    'в этом боте будет происходить рассылка с именем коллеги, '
    'с кем вам нужно организовать встречу.\n'
    '🔁Участники выбираются случайным образом, поэтому вы сможете выпить '
    'кофе с теми, с кем еще не пересекались по работе.\n'
    'Добро пожаловать🥰')

ABOUT_TEXT = '''
В нашей компании есть прекрасная традиция знакомиться за чашечкой горячего кофе в Microsoft Teams или в офисе.
Раз в неделю будет автоматически приходить имя и фамилия коллеги в этот чат-бот, вам остается договориться
о дате и времени встречи в удобном для вас формате.
«Кофе вслепую»- это всегда:
    - Прекрасная компания;
    - Приятный и неожиданный сюрприз;
    - Помощь новым коллегам в адаптации;
    - Новые знакомства.
''' # noqa


async def main_menu(message: Message):
    """Главное меню"""
    await message.answer(
        GREETING_TEXT,
        reply_markup=kb_main_menu())


@main_menu_router.message(F.text == 'О проекте')
async def about_project(message: Message):
    """ Раздел о проекте """
    await message.answer(ABOUT_TEXT)


@main_menu_router.message(F.text == 'Приостановить участие')
async def suspend_participation(message: Message):
    """Приостановление участия."""
    await message.answer('Если вы передумали принимать участие в какую-либо '
                         'неделю или уходите в отпуск, то можно '
                         'приостановить участие в проекте.')
