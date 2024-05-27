from javascript import require, On

print('Что-бы воспользоваться ботом вам нужно: ')
print('1. Зайти на сервер под каким либо никнеймом (это имя для бота)')
print('2. На сервере пройдите процедуру регестарции аккаунта, используя пароль afqwe1623')
print('3. Выйти из игры, и зайти уже под своими данными')
print('4. Ввести данные от аккаунта бота ниже: ')

ip = input("Введите IP сервера, БЕЗ ПОРТА: ")
port = input("Введите PORT сервера, БЕЗ IP: ")
name = input("Введите ник аккаунта бота: ")
print('Бот будет использовать пароль: afqwe1623')
vers = input("Введите версию игры для бота: ")

print('Напишите что нибудь в чат через 30 секунд!')

mineflayer = require('mineflayer')

bot = mineflayer.createBot({
    'host': (ip),
    'port': (port),
    'username': (name),
    'version': (vers)
})

@On(bot, 'chat')
def msgHandler(this, user, message, *args):
    if user != (name):
        bot.chat(f'/login afqwe1623')