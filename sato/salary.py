#import sys
#args = sys.argv
#salary = args[1]
salary = 150

#100万を超えるかの判定
if salary > 100:
    tax = 10 + (salary-100)*0.2
else:
    tax = salary * 0.1

pay = salary-tax

#変数型を指定
tax=int(tax)
pay=int(pay)

#出力
print("支給額:" + str(pay) + "、税額:" + str(tax))
