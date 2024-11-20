from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

individual_specialists = [
    "Алёна Атаманенко",
    "Ольга Павленко",
    "Юлия Андроник",
    "Елена Грызунова",
    "Вероника Быкова",
    "Степуренко Валерия",
    "Мастер-тренер",
    "Анастасия Шевченко",
]

individual_services = [
    "Хатха йога",
    "Здоровая спина"
]

group_specialists =[
    "Анастасия Шевченко",
    "Ольга Павленко",
    "Юлия Андроник",
    "Мастер-тренер",
    "Алёна Атаманенко",
    "Елена Грызунова"
]

group_services = [
    "Йога критического выравнивания",
    "Аэро-йога",
    "Йога-терапия позвоночника",
    "Йога для беременных",
    "Здоровая спина",
    "Йога. Культура движения",
    "Детская аэро-йога",
    "Хатха-йога для начинающих",
    "Утренняя хатха для начинающих",
    "FLY Йога в гамаках"
]

individual_specialists_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=individual_specialist, callback_data=f"individual_specialist_{individual_specialist}")] for individual_specialist in individual_specialists
])

individual_services_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=individual_service, callback_data=f"individual_service_{individual_service}")] for individual_service in individual_services
])

group_specialists_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=group_specialist, callback_data=f"group_specialist_{group_specialist}")] for group_specialist in group_specialists
])

group_services_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=group_service, callback_data=f"group_service_{group_service}")] for group_service in group_services
])