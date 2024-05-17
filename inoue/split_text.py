import sys

args = sys.argv
first_arg = args[1]
second_arg = args[2]

def split_text(text, num):
  index = int(num) - 1
  print(text.split(" ")[index])


split_text(first_arg, second_arg)