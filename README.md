# Random_Coffee_Bot
![screenshot](logo.jpg)

## Описание
Проект Random_Coffee_Bot - это телеграм-бот, который каждую неделю (по понедельникам) предлагает встретиться с одним из людей, зарегистрированных в боте в пределах компании.
Бот делает рассылку с именем и фамилией коллеги, с которым вам нужно организовать встречу. Участники выбираются случайным образом, поэтому вы сможете выпить кофе с теми, с кем еще не пересекались по работе. Подтвержать встречи не нужно, участие по желанию.

В боте Random_Coffee_Bot реализовано:
- Регистрация пользователей (при регистрации происходит проверка уникальности домена почты, т.е. зарегистрироваться могут только сотрудники компании).
- Хранение данных пользователей в БД Postgres. Функции работы с БД реализованы асинхронно для повышения производительности.
- использование библиотеки и сервера Redis для кэширования данных, управления сессиями и реализации очередей сообщений в телеграм-боте, повышая производительность, масштабируемость и отзывчивость бота.
- Каждый пользователь может приостановить или возобновить участие в рассылках для встреч.
- Автоматические еженедельные рассылки (по понедельникам).
- Смена людей случайным образом, исключая повторения. Алгоритм подбора партнера по кофе устроен так, чтобы исключить повторения. Повторение партнеров возможно только в случае, если последняя встреча была более полугода назад.
- Администрирование выполнено двумя способами:
  1. Админ-панель Django (доступ через web-интерфес по адресу: http://127.0.0.1/admin/)
  2. Напрямую из телеграм-бота (позволяет блокировать или разблокировать пользователя по его почте).

## Технолгии
- Python 3.9
- Aiogram 3.4
- Redis 5.0
- Django 4.2
- APScheduler 3.10
- PostgreSQL 13.10
- Requests 2.31

## Запуск проекта
Выполнить установку проект Random_Coffee_Bot на ваш сервер.

В корневой директории проекта <ваш_сервер>/:~random_coffee_bot_andrey создать файл с переменными окружения .env.
Для этого введите команду: ``` sudo touch .env```.
Далее откройте .env-файл с помощью команды ```sudo nano .env``` и заполните его данными по следующему образцу:

```
# Переменные для PostgreSQL
POSTGRES_DB=test_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432

# Переменные для Django-проекта:
SECRET_KEY='django-insecure-7f8jl#&fox9p+zm7@e2!8q66&+%+ex94vwe4razd8t5x+g5!qk'
DEBUG=False
HOST_IP='158.160.16.218'

# Переменные для телеграм ботa
BOT_TOKEN=ваш токен для бота
REDIS_HOST=redis
REDIS_PORT=6379
ALLOWED_DOMAIN=@groupeseb
```

### Обращаем Ваше внимание, что BOT_TOKEN вы должны получить заранее самостоятельно при создании и регистрации бот-чата
### в телеграм сервисе по созданию ботов https://t.me/BotFather

## Использование телеграм-бота:
- Для начала работы перейдите в чат Random_Coffee_Bot, нажмите кнопку "Menu" и всплывающую кнопку "/start".
- Если вы еще не зарегистрированы, то бот предложит вам ввести свои имя и фамилию. После ввода имя и фамилии введите свою корпоративную почту. После успешной регистрации бот ответит вам сообщением "Вы зарегистрированы"
- После регистрации вы автоматически становитесь участником в рассылках для встреч.
- Если вы не хотите продолжать участие, то нажмите кнопку "Приостановить участие". Если же вы желаете продолжить участие, то нажмите кнопку "Возобновить участие".

## Администрирование в админ-панели Django:


## Авторы проекта:
Тен Алексей\
Бойко Максим\
Хлестов Андрей\
Фабиянский Илья\
Стеблев Константин\
