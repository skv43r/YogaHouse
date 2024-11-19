import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config import settings
from handlers import register_handlers
from services.otp_service import OTPService


bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())
otp_service = OTPService(bot)

register_handlers(dp)

async def start_bot() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(start_bot())