from database import session
from datetime import date
from tables import Holiday

# 単体取得
holiday = session.query(Holiday).filter_by(
    holi_date=date(2023, 1, 1)
).first()

print(holiday.holi_date, holiday.holi_text)
