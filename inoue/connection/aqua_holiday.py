import sys
from database import session
from datetime import date, datetime
from tables import Holiday

'''
Input
'''

args = sys.argv

first_arg = args[1]
second_arg = args[2]
third_arg = args[3]

# 日付の入力
input_date = first_arg
input_year = int(input_date[0:4])
input_month = int(input_date[4:6])
input_day = int(input_date[6:])
# 人数の入力（大人・子）
input_adults_count = int(second_arg)
input_children_count = int(third_arg)


'''
Output
'''

# 休日（土日）かどうかを判定
def is_day_off():
  dt = datetime(input_year, input_month, input_day)
  datetime_index = dt.weekday()
  return datetime_index == 5 or datetime_index == 6

# 祝日かどうかを判定
def is_holiday():
    d = date(input_year, input_month, input_day)
    holiday = session.query(Holiday).filter_by(
      holi_date=d
    ).first()
    return holiday != None

# 合計金額を計算
def calc_total_price():
  adult_price = 2400 if is_holiday() or is_day_off() else 2000
  child_price = 1500 if is_holiday() or is_day_off() else 1200
  return adult_price * input_adults_count + child_price * input_children_count

# 結果を出力
result = calc_total_price()
print(result)
