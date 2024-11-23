from models import IndividualSpecialists, IndividualServices, Massage
from database import db

specialists_data = [
    {
        "name": "Мастер-тренер",
        "description": "Преподаватель йоги",
        "photo": "https://assets.yclients.com/masters/origin/a/ad/ad65931d879a1e5_20240825210707.png"
    },
    {
        "name": "Алёна Атаманенко",
        "description": "Преподаватель йоги",
        "photo": "https://example.com/photo2.jpg"
    },
    {
        "name": "Ольга Павленко",
        "description": "Преподаватель йоги",
        "photo": None
    },
    {
        "name": "Вероника Быкова",
        "description": "Преподаватель йоги, массажист",
        "photo": "https://assets.yclients.com/masters/origin/a/ad/ad65931d879a1e5_20240825210707.png"
    },
    {
        "name": "Степуренко Валерия",
        "description": "Преподаватель йоги",
        "photo": "https://assets.yclients.com/masters/origin/a/ad/ad65931d879a1e5_20240825210707.png"
    },
    {
        "name": "Анастасия Шевченко",
        "description": "Преподаватель йоги",
        "photo": "https://assets.yclients.com/masters/origin/a/ad/ad65931d879a1e5_20240825210707.png"
    },
    {
        "name": "Елена Грызунова",
        "description": "Преподаватель йоги",
        "photo": "https://assets.yclients.com/masters/origin/a/ad/ad65931d879a1e5_20240825210707.png"
    },
    {
        "name": "Юлия Андроник",
        "description": "Преподаватель йоги",
        "photo": "https://assets.yclients.com/masters/origin/a/ad/ad65931d879a1e5_20240825210707.png"
    }
]

services_data = [
    {
        "name": "Хатха йога",
        "description": """
            1 ч · Персональные тренировки- это как костюм сшитый на заказ.
            В чем преимущества персоналок перед групповыми тренировками?

            - я работаю с вашим персональным запросом
            - я учитываю ваши исходные данные и индивидуальные физические и психические особенности
            - все время тренировки моё внимание принадлежит только вам
            - я планирую для вас персональный цикл тренировок на определенный срок времени исходя из вашего запроса и индивидуальных особенностей
            - мы выбираем удобное время, место, продолжительность и регулярность занятий
            - в персональной работе мы можем добиться максимальных результатов за минимальное время

            Для кого?

            Для тех, кто ценит свое время, комфорт, индивидуальный подход и прогнозируемый результат... и готов регулярно работать.

            Запросы, с которыми можно ко мне обратиться:

            - общее оздоровление и ОФП (увеличение силы, выносливости и мобильности опорно-двигательного аппарата, профилактика гиподинамии, сердечно-сосудистых заболеваний, заболеваний ОДА и других)
            - работа над определёнными направлениями подвижности, физическими качествами (гибкость, координация, выносливость, сила и т.д.) или темами (шпагаты, прогибы, наклоны, балансы и т.д.)
            - двигательное переобучение (обучение новым двигательным навыкам)
            - работа с дыханием, концентрацией, состоянием ума, техниками сосредоточения — по умолчанию включена во все практики, но по вашему запросу этим аспектам может уделяться больше или меньше внимания

            Занятия подходят для людей любого уровня подготовки без ограничений по состоянию здоровья (если у вас есть диагнозы в ремиссии, и врач разрешает занятия физической культурой — welcome).

            Реабилитацией и лечением не занимаюсь.
        """,
        "price": 3000,
        "photo": "https://assets.yclients.com/main_service_image/basic/a/a3/a3fa859373f5c5b_20240908015458.png"
    },
    {
        "name": "Здоровая спина",
        "description": """
            1 ч · На индивидуальных занятиях я выстраиваю  практику под человека, его особенности здоровья и состояния и, конечно, под определенный запрос, если он есть. 
            Внимательно подхожу к успехам и трудностям практикующего.
            Обучение на йогатерапевта позволяет мне грамотно подобрать техники точечно под определенное заболевание или состояние человека. 
            Практикующий учится чувствовать свое тело, владеть им и избавляется от головных болей, болей в спине, шее и пояснице. 
            Прогресс на индивидуальных занятиях всегда кратно выше.
        """,
        "price": 3000,
        "photo": "https://assets.yclients.com/main_service_image/basic/e/eb/ebc3d23b4d1c8c6_20240813212720.png"
    },
    {
        "name": "Йога для беременных",
        "description": """
            1 ч · Татьяна Мазкина - преподаватель по женской йоге и йоге для беременных. 
            Опыт преподавания 3 года, опыт личной практики 7 лет
            Обучение: Trini yoga school, Yogamed.

            Мое призвание - помогать женщинам создавать гармоничные отношения с самими собой. Я верю, что наше тело - это священный инструмент, способный находить глубокий контакт с нашей внутренней мудростью.


            Плюсы индивидуального подхода в практике йоги для беременных:
            ✅ Персональный подход.
            Инструктор может адаптировать практику йоги под конкретные потребности каждой беременной женщины, учитывая ее физическое состояние, уровень подготовки и индивидуальный запрос.
            ✅  Безопасность и контроль.
            Индивидуальные занятия проходят в  более тесном сопровождении практикующей, что обеспечивает безопасность и создаёт комфортную и доверительную атмосферу
            ✅ Удобное время. 
            Вы можете выбрать для себя комфортное время и удобный формат (онлайн\офлайн)
            ✅ Связь с ребёнком. 
            Во время индивидуальных занятий, инструктор проводит тематические медитации, что помогает создать связь со своим малышом, снизить тревожность и взрастить в себе чувство доверия
        """,
        "price": 3000,
        "photo": "https://assets.yclients.com/main_service_image/basic/c/cf/cf26b900bf1bb68_20240912172950.png"
    }
]

massage_data = [
    {
        "name": "Лечебный массаж",
        "description": """
            1 ч · Массажи проводит Елена Сагир - профессиональный массажист с опытом более 6 лет. С медицинским образованием.
            Работает с лицом,: лифтинг эффект и омоложение. 
            Есть антицеллюлитные программы + баночный массаж, быстрый результат. 
            Отличное самочувствие и счастливое настроение сразу после сеанса!
        """,
        "price": 2000
    },
    {
        "name": "Антицеллюлитный массаж",
        "description": """
            1 ч · Массажи проводит Елена Сагир - профессиональный массажист с опытом более 6 лет. С медицинским образованием.
            Работает с лицом,: лифтинг эффект и омоложение. 
            Есть антицеллюлитные программы + баночный массаж, быстрый результат. 
            Отличное самочувствие и счастливое настроение сразу после сеанса!
        """,
        "price": 2500
    },
    {
        "name": "Спортивный массаж",
        "description": """
            1 ч · Массажи проводит Елена Сагир - профессиональный массажист с опытом более 6 лет. С медицинским образованием.
            Работает с лицом,: лифтинг эффект и омоложение. 
            Есть антицеллюлитные программы + баночный массаж, быстрый результат. 
            Отличное самочувствие и счастливое настроение сразу после сеанса!
        """,
        "price": 3500
    },
    {
        "name": "Массаж лица",
        "description": """
            1 ч · Массажи проводит Елена Сагир - профессиональный массажист с опытом более 6 лет. С медицинским образованием.
            Работает с лицом,: лифтинг эффект и омоложение. 
            Есть антицеллюлитные программы + баночный массаж, быстрый результат. 
            Отличное самочувствие и счастливое настроение сразу после сеанса!
        """,
        "price": 2000
    },
    {
        "name": "Классический массаж",
        "description": """
            1 ч · Массажи проводит Елена Сагир - профессиональный массажист с опытом более 6 лет. С медицинским образованием.
            Работает с лицом,: лифтинг эффект и омоложение. 
            Есть антицеллюлитные программы + баночный массаж, быстрый результат. 
            Отличное самочувствие и счастливое настроение сразу после сеанса!
        """,
        "price": 2500
    },
    {
        "name": "Массаж спины",
        "description": """
            1 ч · Массажи проводит Елена Сагир - профессиональный массажист с опытом более 6 лет. С медицинским образованием.
            Работает с лицом,: лифтинг эффект и омоложение. 
            Есть антицеллюлитные программы + баночный массаж, быстрый результат. 
            Отличное самочувствие и счастливое настроение сразу после сеанса!
        """,
        "price": 2000
    },
    {
        "name": "Баночный массаж",
        "description": """
            1 ч · Массажи проводит Елена Сагир - профессиональный массажист с опытом более 6 лет. С медицинским образованием.
            Работает с лицом,: лифтинг эффект и омоложение. 
            Есть антицеллюлитные программы + баночный массаж, быстрый результат. 
            Отличное самочувствие и счастливое настроение сразу после сеанса!
        """,
        "price": 2000
    },
    {
        "name": "Массаж головы",
        "description": """
            1 ч · Массажи проводит Елена Сагир - профессиональный массажист с опытом более 6 лет. С медицинским образованием.
            Работает с лицом,: лифтинг эффект и омоложение. 
            Есть антицеллюлитные программы + баночный массаж, быстрый результат. 
            Отличное самочувствие и счастливое настроение сразу после сеанса!
        """,
        "price": 1500
    },
    {
        "name": "Расслабляющий массаж",
        "description": """
            1 ч · Массажи проводит Елена Сагир - профессиональный массажист с опытом более 6 лет. С медицинским образованием.
            Работает с лицом,: лифтинг эффект и омоложение. 
            Есть антицеллюлитные программы + баночный массаж, быстрый результат. 
            Отличное самочувствие и счастливое настроение сразу после сеанса!
        """,
        "price": 2500
    },
    {
        "name": "Массаж ног",
        "description": """
            1 ч · Массажи проводит Елена Сагир - профессиональный массажист с опытом более 6 лет. С медицинским образованием.
            Работает с лицом,: лифтинг эффект и омоложение. 
            Есть антицеллюлитные программы + баночный массаж, быстрый результат. 
            Отличное самочувствие и счастливое настроение сразу после сеанса!
        """,
        "price": 1500
    },
    {
        "name": "Массаж шейно-воротниковой зоны",
        "description": """
            1 ч · Массажи проводит Елена Сагир - профессиональный массажист с опытом более 6 лет. С медицинским образованием.
            Работает с лицом,: лифтинг эффект и омоложение. 
            Есть антицеллюлитные программы + баночный массаж, быстрый результат. 
            Отличное самочувствие и счастливое настроение сразу после сеанса!
        """,
        "price": 1500
    }
]

def insert_data():
    with next(db.get_session()) as session:
        for specialist in specialists_data:
            specialist_entry = IndividualSpecialists(**specialist)
            session.add(specialist_entry)

        for service in services_data:
            service_entry = IndividualServices(**service)
            session.add(service_entry)
            
        for massage in massage_data:
            massage_entry = Massage(**massage)
            session.add(massage_entry)

        session.commit()

if __name__ == "__main__":
    insert_data()