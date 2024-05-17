import sys
import math
from module.func_salary import calcAmount

args = sys.argv

def parallel_salary(salary_list):
  for salary in salary_list:
    result = calcAmount(int(salary))
    allowance = result["allowance"]
    tax_amount = result["tax_amount"]
    print(f"給与:{salary}、支給額:{math.floor(allowance)}、税額:{math.floor(tax_amount)}")

parallel_salary(args[1:len(args)])