import asyncio
from aiogram import Bot as _Bot
from dotenv import load_dotenv
import os

class Bot():
    def __init__(self, BOT_TOKEN=None, CHAT_ID=None) -> None:
        if not BOT_TOKEN or not CHAT_ID:
            load_dotenv('secret.env')
            BOT_TOKEN = os.environ['TELEGRAM_TOKEN']
            CHAT_ID = os.environ['TELEGRAM_CHAT_ID']
        self.bot = _Bot(token=BOT_TOKEN)
        self.chat_id = CHAT_ID
    
    async def send(self, text):
        await self.bot.send_message(self.chat_id, text)


if __name__ == '__main__':
    a = Bot()
    asyncio.run(a.send('hello'))