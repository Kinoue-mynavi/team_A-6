from db.tables import Holiday
from db.database import session

# 単体取得
holiday_list = session.query(Holiday).all()

for item in holiday_list:
    print(item.holi_date, item.holi_text)

print(session)