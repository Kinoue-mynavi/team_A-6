import sys
import datetime

args = sys.argv

date = args[1]
year = int(date[0:4])
month = int(date[4:6])
day = int(date[6:])

numOfAdults = int(args[2])
numOfChildren = int(args[3])

def is_holiday(d: int):
  return d == 5 or d == 6

weekday = datetime.datetime(year, month, day).weekday()
adult_price = 2400 if is_holiday(weekday) else 2000
child_price = 1500 if is_holiday(weekday) else 1200

totalPrice = adult_price * numOfAdults + child_price * numOfChildren

print(totalPrice)
