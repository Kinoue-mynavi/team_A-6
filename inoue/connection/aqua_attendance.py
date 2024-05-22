import sys
from database import session
from datetime import date
from tables import Attendnum

args = sys.argv

arg_date = args[1]
arg_year = int(arg_date[0:4])
arg_month = int(arg_date[4:6])
arg_day = int(arg_date[6:])

num_of_adults = int(args[2])
num_of_children = int(args[3])

# --------------------------- #

# 全権取得
attendnum_list = session.query(Attendnum).all()
attendnum_length = len(attendnum_list)

def has_equel_date():
    if len(attendnum_list) <= 0: return False
    for item in attendnum_list:
        return date(arg_year, arg_month, arg_day) == item.entry_date

def add_attendance():
    sequence = attendnum_length + 1 if has_equel_date() else attendnum_length
    holiday = Attendnum(
        entry_date = date(arg_year, arg_month, arg_day),
        seq = sequence, # 合計データ数 + 1
        adult = num_of_adults,
        child = num_of_children
    )
    session.add(holiday)
    session.commit()

# 追加
add_attendance()

# 追加確認
# HACK: 他によい確認方法ありそう？？
attendnum_list = session.query(Attendnum).all()

for attendnum_item in attendnum_list:
    print(
        attendnum_item.entry_date,
        attendnum_item.seq,
        attendnum_item.adult,
        attendnum_item.child
    )
