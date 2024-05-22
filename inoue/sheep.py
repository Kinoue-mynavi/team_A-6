import sys

args = sys.argv
first_arg = int(args[1])

def repeat(num: int):
  for i in range(num):
    count = i + 1
    print(f"ひつじが{count}匹")

repeat(first_arg)