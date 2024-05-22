from database import session
from tables import Holiday

# 全権取得
holiday_list = session.query(Holiday).all()

for holiday in holiday_list:
    print(holiday.holi_date, holiday.holi_text)
