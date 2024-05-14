import sys
import math
from typing import int,str,bool

args = sys.argv
# 入力をintegerへ変換
first_arg = int(args[1])

# -----------------------

def proccessing(salary: int):
    limit = 1000000
    tax_amount = salary * 0.1 if salary <= limit else limit * 0.1 + (salary - limit) * 0.2
    allowance = salary - tax_amount
    print(f"支給額:{math.floor(allowance)}、税額:{math.floor(tax_amount)}")

# -----------------------

num: int = "kdkdk"

# 処理を実行する
def implement(arg):
    proccessing(arg)

implement(first_arg)