from aiogram import Dispatcher, types
from aiogram.filters import Command
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery
from aiogram_calendar import SimpleCalendar, SimpleCalendarCallback
from aiogram.fsm.context import FSMContext
from services.menu import menu_keyboard, individual_service_keyboard, type_keyboard
from services.inline_keyboards import individual_specialists_keyboard, individual_services_keyboard, massage_list_keyboard, massage_master_keyboard, time_keyboard

class CallbackDataForSpecialist(CallbackData, prefix="ind_spec"):
    specialist_id: int


def register_handlers(dp: Dispatcher):
    @dp.message(Command("start"))
    async def cmd_start(message: types.Message):
        await message.answer("Добро пожаловать! Выберите опцию:", reply_markup=menu_keyboard)

    @dp.message(lambda message: message.text == "Индивидуальные услуги")
    async def handle_individual_services_menu(message: types.Message):
        await message.answer("Выберите опцию:", reply_markup=individual_service_keyboard)
    
    @dp.message(lambda message: message.text == "Главное меню")
    async def handle_main_menu(message: types.Message):
        await message.answer("Выберите опцию:", reply_markup=menu_keyboard)
    
    @dp.message(lambda message: message.text == "Выбрать услуги")
    async def handle_services_type_menu(message: types.Message):
        await message.answer("Выберите тип услуги:", reply_markup=type_keyboard)

    @dp.message(lambda message: message.text == "Индивидуальные занятия")
    async def handle_individual_services_menu(message: types.Message):
            await message.answer("Выберите услугу:", reply_markup=individual_services_keyboard)

    
# Выбрать специалиста

    @dp.message(lambda message: message.text == "Выбрать специалиста")
    async def handle_individual_specialists_menu(message: types.Message):
        await message.answer("Выберите специалиста:", reply_markup=individual_specialists_keyboard)


# Выбор услуги

    @dp.callback_query(lambda c: c.data and c.data.startswith("individual_specialist"))
    async def handle_specific_service(callback_query: types.CallbackQuery):
        await callback_query.message.edit_text(
            text=f"Выберите услугу:",
            reply_markup=individual_services_keyboard
        )

    @dp.callback_query(lambda c: c.data and c.data.startswith("individual_services_"))
    async def handle_specific_specialist(callback_query: types.CallbackQuery):
        await callback_query.message.edit_text(
            text=f"Выберите дату:",
            reply_markup= await SimpleCalendar().start_calendar()
        )

# Массаж

    @dp.message(lambda message: message.text == "Массажи")
    async def handle_massage_list__menu(message: types.Message):
        await message.answer("Выберите специалиста:", reply_markup=massage_list_keyboard)
    
    @dp.callback_query(lambda c: c.data and c.data.startswith("massage_list"))
    async def handle_massage_list(callback_query: types.CallbackQuery):
        await callback_query.message.edit_text(
            text=f"Выберите мастера:",
            reply_markup=massage_master_keyboard
        )

    @dp.callback_query(lambda c: c.data and c.data.startswith("massage_master"))
    async def handle_date_check(callback_query: types.CallbackQuery):
        await callback_query.message.edit_text(
            text=f"Выберите дату:",
            reply_markup= await SimpleCalendar().start_calendar()
        )
    
    @dp.callback_query(SimpleCalendarCallback.filter())
    async def process_simple_calendar(callback_query: CallbackQuery, callback_data: dict, state: FSMContext):
        selected, date = await SimpleCalendar().process_selection(callback_query, callback_data)
        if selected:
            await state.update_data(selected_date=date.strftime('%d-%m-%Y'))
            await callback_query.message.edit_text(
                text=f"Вы выбрали {date.strftime('%d-%m-%Y')}, теперь выберите удобное для вас время:",
                reply_markup=time_keyboard
            )

    @dp.callback_query(lambda c: c.data and c.data.startswith("time_"))
    async def process_time_selection(callback_query: CallbackQuery, state: FSMContext):
        selected_time = callback_query.data.split("_")[1]
        user_data = await state.get_data()
        selected_date = user_data.get("selected_date", "дата не выбрана")
        await callback_query.message.edit_text(
            text=f"Вы записаны на {selected_date} в {selected_time}.\nЖдем вас!"
        )