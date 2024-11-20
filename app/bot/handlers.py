from aiogram import Dispatcher, types
from aiogram.filters import Command
from services.menu import menu_keyboard, individual_service_keyboard
from services.inline_keyboards import individual_specialists_keyboard, individual_services_keyboard, group_specialists_keyboard, group_services_keyboard

def register_handlers(dp: Dispatcher):
    @dp.message(Command("start"))
    async def cmd_start(message: types.Message):
        await message.answer("Добро пожаловать! Выберите опцию:", reply_markup=menu_keyboard)

    @dp.message(lambda message: message.text == "Индивидуальные услуги")
    async def handle_individual_services(message: types.Message):
        await message.answer("Выберите опцию:", reply_markup=individual_service_keyboard)
    
    @dp.message(lambda message: message.text == "Главное меню")
    async def handle_main_menu(message: types.Message):
        await message.answer("Выберите опцию:", reply_markup=menu_keyboard)
    
    @dp.message(lambda message: message.text == "Выбрать специалиста")
    async def handle_specialists_menu(message: types.Message):
        await message.answer("Выберите специалиста:", reply_markup=individual_specialists_keyboard)
    
    @dp.message(lambda message: message.text == "Выбрать услуги")
    async def handle_specialists_menu(message: types.Message):
        await message.answer("Выберите специалиста:", reply_markup=individual_services_keyboard)