import sys

args = sys.argv
first_arg = int(args[1])

def repeat(num: int):
  sum = 0
  while sum <= 100:
    if sum == 100:
      print("Just 100!")
      break
    sum += num

  if sum != 100:
    print("Over!")

repeat(first_arg)