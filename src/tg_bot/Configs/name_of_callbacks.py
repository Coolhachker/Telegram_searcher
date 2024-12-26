from dataclasses import dataclass


@dataclass
class NameOfCallbacks:
    callback_for_delete_chat_button = 'delete_chat'
    callback_for_add_chat_button = 'add_chat'
    callback_for_comeback_button = 'comeback'
    callback_for_right_button_chats = "right_button_chats="
    callback_for_left_button_chats = 'left_button_chats='
    callback_for_delete_chat_index_button = 'delete_chat_index='