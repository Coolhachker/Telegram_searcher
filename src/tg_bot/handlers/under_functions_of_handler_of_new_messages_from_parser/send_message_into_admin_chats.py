from aiogram import Bot


async def send_messages_into_admin_chats(message: str, chats: list, bot: Bot):
    for chat in chats:
        try:
            await bot.send_message(chat[0], message)
        except:
            continue