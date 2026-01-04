from telethon import TelegramClient


api_id =  # число без лапок
api_hash =

# Створюємо клієнт (це виправляє NameError)
client = TelegramClient('mysession', api_id, api_hash)


async def main():
    print("Програма запущена...")

    # 1. Отримання учасників чату
    # Використовуйте username групи БЕЗ https://t.me/
    chat_username = '+1TxlapbiJ7g1ZmYy'

    print(f"Отримую список учасників з {chat_username}...")
    async for user in client.iter_participants(chat_username, limit=10):
        print(f"Знайдено: {user.first_name} (@{user.username})")

    # 2. Відправка повідомлення
    # Тут також краще просто username контакту
    await client.send_message('arozanova', 'Слава Україні!')
    print("Повідомлення надіслано!")


# Запуск клієнта
with client:
    client.loop.run_until_complete(main())