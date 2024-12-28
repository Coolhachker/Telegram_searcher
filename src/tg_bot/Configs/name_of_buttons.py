from dataclasses import dataclass


@dataclass
class NamesOfButtons:
    reply_button_chats = 'ℹ️ Чаты'
    add_chat_button = '➕️ добавить чат'
    delete_chat_button = '➖️ удалить чат'

    comeback_button = "Вернуться"
    right_button = "⏩️"
    left_button = "⏪"
    key_words_button = "📑 Ключевые слова"

    add_key_world_button = "➕️ добавить ключевое слово"
    delete_key_world_button = '➖️ удалить ключевое слово'
    change_key_world_button = '🔄 Изменить ключевое слово'

    parser_button = '🔎 Парсер'
    turn_on_button = '🟢 Включить парсер'
    turn_off_parser = '🔴 Выключить парсер'

    ban_list_button = '📑 Бан-лист'
    add_member_into_ban_list_button = '➕️ Добавить в бан лист'
    delete_member_from_ban_list_button = '➖️ Удалить из бан листа'


