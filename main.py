import datetime
import os
import telepot
from telepot.loop import MessageLoop
from time import sleep
import sys
import time
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

from config.telegram import init
from modules.network.ip import get_local_ip, get_public_ip
from modules.cpu.stat import get_cpu_stat
from telepot.namedtuple import InlineQueryResultArticle, InputTextMessageContent

now = datetime.datetime.now()


def on_inline_query(msg):
    query_id, from_id, query_string = telepot.glance(
        msg, flavor='inline_query')
    print('Inline Query:', query_id, from_id, query_string)

    articles = [InlineQueryResultArticle(
        id='abc',
        title='ABC',
        input_message_content=InputTextMessageContent(
            message_text='Hello'
        )
    )]

    bot.answerInlineQuery(query_id, articles)


def on_chosen_inline_result(msg):
    result_id, from_id, query_string = telepot.glance(
        msg, flavor='chosen_inline_result')
    print('Chosen Inline Result:', result_id, from_id, query_string)


def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(
        msg, flavor='callback_query')

    if query_data == 'local_ip':
        bot.sendMessage(from_id, get_local_ip())
    elif query_data == 'public_ip':
        bot.sendMessage(from_id, get_public_ip())


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    command = msg['text']

    print(command)

    if content_type == 'text':
        if command == 'hi':
            bot.sendMessage(
                chat_id, f"Hi! Valeriann here. How can I help you?")
        elif command == 'get ip':
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='Local', callback_data='local_ip')],
                [InlineKeyboardButton(
                    text='Public', callback_data='public_ip')],
            ])
            bot.sendMessage(chat_id, 'Select option', reply_markup=keyboard)
        elif command == 'get machine user':
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='Login', callback_data='local_ip')],
                [InlineKeyboardButton(
                    text='Logout', callback_data='public_ip')],
                [InlineKeyboardButton(
                    text='Lock', callback_data='public_ip')],
                [InlineKeyboardButton(
                    text='Switch User', callback_data='public_ip')],
                [InlineKeyboardButton(
                    text='Switch VT', callback_data='public_ip')],
            ])
            bot.sendMessage(chat_id, 'Select option', reply_markup=keyboard)
        elif command == 'get local datetime':
            bot.sendMessage(chat_id, f"Date: {now}")
        elif command == 'help':
            text = '''ValeriannBot, version 0.0.2 \nThis bot is designed internally for personal use. Type `help' to see this list.\nType `help name' to find out more about the function `name'.\nUse `info bot' to find out more about the bot in general.\n\nA star (*) next to a name means that the command is disabled.'''
            bot.sendMessage(chat_id, text)
        elif command == 'get cpu stat':
            cpu_stat = get_cpu_stat()
            bot.sendMessage(chat_id, cpu_stat, parse_mode=bot.ParseMode.HTML)
        elif command == 'net restart':
            bot.sendMessage(chat_id, f"Restarting network...")
            os.system('sudo systemctl restart networking')
        elif command == 'restart cpu':
            bot.sendMessage(chat_id, f"Restarting CPU...")
            os.system('sudo reboot')
            bot.sendMessage(chat_id, f"CPU restarted")


if __name__ == '__main__':
    print(':: Initializing ::')
    bot = init()

    MessageLoop(
        bot, {
            'chat': handle,
            'callback_query': on_callback_query,
            'inline_query': on_inline_query,
            'chosen_inline_result': on_chosen_inline_result
        }).run_as_thread()

    while True:
        sleep(10)
