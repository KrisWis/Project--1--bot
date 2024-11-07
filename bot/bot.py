import logging
from aiogram import Bot, Dispatcher, types, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
from aiogram.filters import CommandStart

API_TOKEN = '7841539658:AAFIv4Hg4uHG5GbunQq4DAaIbryYUXYwKtI'

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создание объекта бота и диспетчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher()
router = Router()

# Определение состояний
class GameStates(StatesGroup):
    waiting_for_choice = State()

async def start_game(message: types.Message, state: FSMContext):
    await message.answer("Добро пожаловать в игру 'Камень, ножницы, бумага'! Выберите: камень, ножницы или бумагу.")
    await state.set_state(GameStates.waiting_for_choice)

async def handle_choice(message: types.Message):
    user_choice = message.text.lower()
    if user_choice not in ['камень', 'ножницы', 'бумага']:
        await message.answer("Пожалуйста, выберите: камень, ножницы или бумагу.")
    else:
        await message.answer(f"Вы выбрали: {user_choice}. Теперь играйте на веб-приложении!")
        
        keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
            [types.InlineKeyboardButton(text="Перейти в игру", web_app=types.WebAppInfo(url="https://project---1-kriswis.amvera.io/"))]
        ])
        
        await message.answer("Нажмите на кнопку ниже, чтобы начать игру:", reply_markup=keyboard)

async def main():
    dp.include_router(router)
    
    router.message.register(start_game, CommandStart())
    router.message.register(handle_choice, GameStates.waiting_for_choice)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
