from aiogram import Bot, Dispatcher
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.tg_bot.Configs.States import States
from databases.sqlite import sqlite3_client
from src.tg_bot.Configs.templates import \
(
    save_url_message,
    incorrect_url_message,
    repeat_url,
    save_key_word_message,
    repeat_key_word,
    save_ban_user_message,
    repeat_ban_user,
    incorrect_ban_user

)
from src.tg_bot.keyboards.start_keyboard import return_start_keyboard

from src.tg_bot.Configs.templates import message_on_success_change_key_word


def handle_states(dispatcher: Dispatcher, bot: Bot):
    @dispatcher.message(States.get_url_of_chat)
    async def get_url_of_chat(message: Message, state: FSMContext):
        url = message.text
        if url.startswith('https://') or url.startswith('@'):
            try:
                sqlite3_client.add_chat_into_table(url)
                await bot.send_message(message.chat.id, save_url_message, reply_markup=return_start_keyboard())
                await state.clear()
            except:
                await bot.send_message(message.chat.id, repeat_url)

        else:
            await bot.send_message(message.chat.id, text=incorrect_url_message)

    @dispatcher.message(States.get_key_word)
    async def get_key_word(message: Message, state: FSMContext):
        key_word = message.text
        try:
            sqlite3_client.add_key_word(key_word)
            await bot.send_message(message.chat.id, save_key_word_message, reply_markup=return_start_keyboard())
            await state.clear()
        except:
            await bot.send_message(message.chat.id, repeat_key_word)

    @dispatcher.message(States.get_change_key_word)
    async def get_changed_key_word(message: Message, state: FSMContext):
        new_key_word = message.text
        key_word = await state.get_data()
        key_word = key_word['key_word']

        try:
            sqlite3_client.update_key_word(key_word, new_key_word)

            await bot.send_message(message.chat.id, message_on_success_change_key_word, reply_markup=return_start_keyboard())
            await state.clear()
        except:
            await bot.send_message(message.chat.id, repeat_key_word)

    @dispatcher.message(States.get_nickname_of_spamer)
    async def get_nickname_of_spamer(message: Message, state: FSMContext):
        if message.text.startswith('@'):
            try:
                sqlite3_client.add_ban_member_into_table(message.text[1:])
                await bot.send_message(message.chat.id, save_ban_user_message, reply_markup=return_start_keyboard())
                await state.clear()
            except:
                await bot.send_message(message.chat.id, repeat_ban_user)
        else:
            await bot.send_message(message.chat.id, incorrect_ban_user)
