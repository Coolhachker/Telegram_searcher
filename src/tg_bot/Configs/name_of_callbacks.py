from dataclasses import dataclass


@dataclass
class NameOfCallbacks:
    callback_for_delete_chat_button = 'delete_chat'
    callback_for_add_chat_button = 'add_chat'
    callback_for_comeback_button = 'comeback'
    callback_for_right_button_chats = "right_button_chats="
    callback_for_left_button_chats = 'left_button_chats='
    callback_for_delete_chat_index_button = 'delete_chat_index='

    callback_for_add_key_word_button = 'add_key_word'
    callback_for_delete_key_word_button = 'delete_key_word'
    callback_for_change_key_word_button = 'change_key_word'

    callback_for_right_button_key_words = "right_button_key_words="
    callback_for_left_button_key_words = 'left_button_key_words='
    callback_for_delete_key_word_index_button = 'delete_key_word_index='

    callback_for_change_key_word_index_button = 'change_key_word_index='