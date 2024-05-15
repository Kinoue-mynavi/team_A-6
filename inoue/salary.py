import sys
import math

args = sys.argv
first_arg = int(args[1])

MAX_AMOUNT = 1000000

def calcAmount(salary: int):
  tax_amount = salary * 0.1 if salary <= MAX_AMOUNT else MAX_AMOUNT * 0.1 + (salary - MAX_AMOUNT) * 0.2
  allowance = salary - tax_amount

  return {
    "tax_amount": tax_amount,
    "allowance": allowance,
  }

result = calcAmount(first_arg)
res_allowance = result["allowance"]
res_tax_amount = result["tax_amount"]

print(f"支給額:{math.floor(res_allowance)}、税額:{math.floor(res_tax_amount)}")