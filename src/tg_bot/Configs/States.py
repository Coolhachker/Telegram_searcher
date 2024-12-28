from aiogram.fsm.state import StatesGroup, State


class States(StatesGroup):
    get_url_of_chat = State()
    get_key_word = State()
    get_change_key_word = State()
    get_nickname_of_spamer = State()