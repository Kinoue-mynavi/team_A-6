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