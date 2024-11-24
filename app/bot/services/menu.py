from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

buttons = [
    ["Индивидуальные услуги", "Чат с администратором"],
    ["Колесо фортуны", "Реферальная программа"],
    ["Групповые события", "О филиале"],
    ["Мои записи"]
]

individual_service_buttons = [
    ["Выбрать специалиста", "Выбрать дату и время"],
    ["Выбрать услуги", "Главное меню"]
]

individual_types_buttons = [
    ["Индивидуальные занятия", "Массажи"],
    ["Главное меню"]
]


def create_keyboard(items):
    return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text=item) for item in row] for row in items
])

menu_keyboard = create_keyboard(buttons)
individual_service_keyboard = create_keyboard(individual_service_buttons)
type_keyboard = create_keyboard(individual_types_buttons)