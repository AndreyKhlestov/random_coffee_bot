import os
import logging

from dotenv import load_dotenv

load_dotenv()

"""Logging levels"""
DEBUG = os.getenv('DEBUG')

"""Tokens"""
BOT_TOKEN = os.getenv('BOT_TOKEN')

"""Domain"""
ALLOWED_DOMAIN = os.getenv('ALLOWED_DOMAIN')

logging.basicConfig(level=logging.DEBUG if DEBUG else logging.INFO)

"""Greeting text"""
GREETING_TEXT = (
    'Что умеет этот бот?'
    '\n☕️Мы продолжаем нашу прекрасную традицию знакомиться за чашечкой '
    'горячего кофе или чая.'
    '\n🗓️ С кем ты разделишь капучино - решает случай. Каждый понедельник '
    'в этом боте будет происходить рассылка с именем коллеги, '
    'с кем вам нужно организовать встречу.'
    '\n🔁Участники выбираются случайным образом, поэтому вы сможете выпить '
    'кофе с теми, с кем еще не пересекались по работе.'
    '\nДобро пожаловать🥰')
