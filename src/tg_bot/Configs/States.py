from aiogram.fsm.state import StatesGroup, State


class States(StatesGroup):
    get_url_of_chat = State()
    get_key_word = State()