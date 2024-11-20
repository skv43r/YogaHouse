from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

buttons = [
    ["Индивидуальные услуги", "Чат с администратором"],
    ["Колесо фортуны", "Реферальная программа"],
    ["Групповые события", "О филиале"],
    ["Мои записи"]
]

menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text=button) for button in row] for row in buttons
])

individual_service_buttons = [
    ["Выбрать специалиста", "Выбрать дату и время"],
    ["Выбрать услуги", "Главное меню"]
]

individual_service_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text=button) for button in row] for row in individual_service_buttons
])