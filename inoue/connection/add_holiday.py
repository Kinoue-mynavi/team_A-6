from database import session
from datetime import date
from tables import Holiday

holiday = Holiday(
    holi_date = date(2023, 1, 1),
    holi_text = "お正月"
)

session.add(holiday)
session.commit()

