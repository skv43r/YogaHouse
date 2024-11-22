from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.models import IndividualSpecialists, IndividualServices, Massage
from database.database import db
from sqlmodel import select

def get_items_from_db(session, model):
    queru = select(model.id, model.name)
    return [{"id": row.id, "name": row.name} for row in session.exec(queru)]

def create_keyboard(items, callback_prefix):
    return InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=item["name"], callback_data=f"{callback_prefix}_{item['id']}")] for item in items
])

def get_master_from_db(session, model, id):
    query = select(model.id, model.name).where(model.id == id)
    master = session.exec(query).first()
    return [{"id": master.id, "name": master.name}]

def generate_time_keyboard():
    times = [
        "9:00", "9:30", "10:00", "10:30", 
        "11:00", "11:30", "12:00", "12:30", 
        "13:00", "13:30", "14:00", "14:30", 
        "15:00", "15:30", "16:00", "16:30", 
        "17:00", "17:30", "18:00", "18:30", 
        "19:00", "19:30", "20:00", "20:30"
    ]
    rows = [times[i:i + 4] for i in range(0, len(times), 4)]
    inline_keyboard = [[InlineKeyboardButton(text=time, callback_data=f"time_{time}") for time in row] for row in rows]

    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)

def generate_keyboards():
    with next(db.get_session()) as session:
        individual_specialists = get_items_from_db(session, IndividualSpecialists)
        individual_services = get_items_from_db(session, IndividualServices)
        massage_list = get_items_from_db(session, Massage)
        massage_master = get_master_from_db(session, IndividualSpecialists, 1)

        individual_specialists_keyboard = create_keyboard(individual_specialists, "individual_specialist")
        individual_services_keyboard = create_keyboard(individual_services, "individual_services")
        massage_list_keyboard = create_keyboard(massage_list, "massage_list")
        massage_master_keyboard = create_keyboard(massage_master, "massage_master")
        
        return individual_specialists_keyboard, individual_services_keyboard, massage_list_keyboard, massage_master_keyboard
    

individual_specialists_keyboard, individual_services_keyboard, massage_list_keyboard, massage_master_keyboard = generate_keyboards()
time_keyboard = generate_time_keyboard()
