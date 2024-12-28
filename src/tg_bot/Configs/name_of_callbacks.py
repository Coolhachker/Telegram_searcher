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

    turn_off_parser = 'turn_off'
    turn_on_parser = 'turn_on'

    callback_for_add_member_into_ban_list_button = 'add_member_into_ban_list'
    callback_for_delete_member_from_ban_list_button = "delete_member_from_ban_list"

    callback_for_right_button_ban_list = "right_button_ban_list="
    callback_for_left_button_ban_list = 'left_button_ban_list='
    callback_for_delete_ban_list_index_button = 'delete_ban_list_index='