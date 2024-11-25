from aiogram import Dispatcher, types
from aiogram.filters import Command
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery
from aiogram_calendar import SimpleCalendar, SimpleCalendarCallback
from aiogram.fsm.context import FSMContext
from sqlalchemy import select
from services.menu import menu_keyboard, type_keyboard
from services.inline_keyboards import individual_specialists_keyboard, individual_services_keyboard, massage_list_keyboard, massage_master_keyboard, time_keyboard, admin_chat_keyboard, about_keyboard

from database.models import IndividualSpecialists, IndividualServices, Massage, Booking
from database.database import db

class CallbackDataForSpecialist(CallbackData, prefix="ind_spec"):
    specialist_id: int


def register_handlers(dp: Dispatcher):
    @dp.message(Command("start"))
    async def cmd_start(message: types.Message):
        await message.answer("Добро пожаловать! Выберите опцию:", reply_markup=menu_keyboard)

    @dp.message(lambda message: message.text == "Индивидуальные услуги")
    async def handle_individual_services_menu(message: types.Message):
        await message.answer("Выберите опцию:", reply_markup=type_keyboard)
    
    @dp.message(lambda message: message.text == "Главное меню")
    async def handle_main_menu(message: types.Message):
        await message.answer("Выберите опцию:", reply_markup=menu_keyboard)
    
    @dp.message(lambda message: message.text == "Индивидуальные занятия")
    async def handle_individual_services_menu(message: types.Message):
            await message.answer("Выберите услугу:", reply_markup=individual_services_keyboard)

# Выбор услуги

    @dp.callback_query(lambda c: c.data and c.data.startswith("individual_services_"))
    async def handle_specific_service(callback_query: types.CallbackQuery, state: FSMContext):
        service_id = callback_query.data.split("_")[-1]
        with next(db.get_session()) as session:
            query = select(IndividualServices.name).where(IndividualServices.id == service_id)
            name = session.exec(query).scalar()
            await state.update_data(selected_service=name)
        await callback_query.message.edit_text(
            text=f"Выберите специалиста:",
            reply_markup=individual_specialists_keyboard
        )

    @dp.callback_query(lambda c: c.data and c.data.startswith("individual_specialist"))
    async def handle_specific_specialist(callback_query: types.CallbackQuery, state: FSMContext):
        master_id = callback_query.data.split("_")[-1]
        with next(db.get_session()) as session:
            query = select(IndividualSpecialists.name).where(IndividualSpecialists.id == master_id)
            name = session.exec(query).scalar()
            await state.update_data(selected_master=name)
        await callback_query.message.edit_text(
            text=f"Выберите дату:",
            reply_markup= await SimpleCalendar().start_calendar()
        )

# Массаж

    @dp.message(lambda message: message.text == "Массажи")
    async def handle_massage_list__menu(message: types.Message):
        await message.answer("Выберите специалиста:", reply_markup=massage_list_keyboard)
    
    @dp.callback_query(lambda c: c.data and c.data.startswith("massage_list"))
    async def handle_massage_list(callback_query: types.CallbackQuery, state: FSMContext):
        massage_id = callback_query.data.split("_")[-1]
        with next(db.get_session()) as session:
            query = select(Massage.name).where(Massage.id == massage_id)
            name = session.exec(query).scalar()
            await state.update_data(selected_service=name)
        
        await callback_query.message.edit_text(
            text=f"Выберите мастера:",
            reply_markup=massage_master_keyboard
        )

    @dp.callback_query(lambda c: c.data and c.data.startswith("massage_master"))
    async def handle_date_check(callback_query: types.CallbackQuery, state: FSMContext):
        master_id = callback_query.data.split("_")[-1]
        with next(db.get_session()) as session:
            query = select(IndividualSpecialists.name).where(IndividualSpecialists.id == master_id)
            name = session.exec(query).scalar()
            await state.update_data(selected_master=name)

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
        selected_date = user_data.get("selected_date")
        selected_master = user_data.get("selected_master")
        selected_service = user_data.get("selected_service")
        user_id = callback_query.from_user.id
        await callback_query.message.edit_text(
            text=(
                f"Вы записаны на: *{selected_service}*\n"
                f"К мастеру: *{selected_master}*\n"
                f"Ждем вас *{selected_date}* в *{selected_time}*!"
            ),
            parse_mode="Markdown"
        )
        with next(db.get_session()) as session:
            new_booking = Booking(
                user_id=user_id,
                service=selected_service,
                master=selected_master,
                date=selected_date,
                time=selected_time
            )
            session.add(new_booking)
            session.commit()

    @dp.message(lambda message: message.text == "Чат с администратором")
    async def handle_admin_chat(message: types.Message):
        await message.answer("Связаться с админимстратором", reply_markup=admin_chat_keyboard)

    @dp.message(lambda message: message.text == "Мои записи")
    async def handle_my_bookings(message: types.Message):
        user_id = message.from_user.id
        with next(db.get_session()) as session:
            bookings = session.scalars(select(Booking).where(Booking.user_id == user_id)).all()
            if not bookings:
                await message.answer("У вас пока нет записей.")
            else:
                response = "Ваши записи:\n\n"
                for booking in bookings:
                    print(f"Тип объекта: {type(booking)}")
                    print(f"Атрибуты: {dir(booking)}")
                    print(f"Данные: {booking}")
                    
                    response += (
                        f"Услуга: *{booking.service}*\n"
                        f"Мастер: *{booking.master}*\n"
                        f"Дата: *{booking.date}*\n"
                        f"Время: *{booking.time}*\n\n"
                    )

                await message.answer(response, parse_mode="Markdown")

    @dp.message(lambda message: message.text == "О филиале")
    async def handle_about(message: types.Message):
        await message.answer(
            text=
"""Студия йоги в центре Краснодара - *Йога Хом*

*Часы работы:*
Пн. - Вс.: 9:00-21:00

*Контакты:*
[+7 929 827-40-24](tel:+79298274024)

Попробуйте захватывающие занятия йогой в гамаках, улучшите гибкость и силу с _Аштанга йогой_, насладитесь мягкими практиками _Soft йоги_ или восстановите здоровье спины с помощью _Йогатерапии позвоночника_. Присоединяйтесь к нам и найдите свой путь к внутреннемуравновесию и благополучию.

Возраст и уровень подготовки не важен, мы ждём всех, до встречи на ковриках!""",
            parse_mode="Markdown",
            reply_markup=about_keyboard
        )
