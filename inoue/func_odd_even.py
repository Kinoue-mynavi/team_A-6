import sys
args = sys.argv

def is_even(num):
  return num % 2 == 0

def print_odd_or_even(numbers):
  for numStr in numbers:
    num = int(numStr) # ここでキャストしたくない、、、。（→入力側でmapする）
    result = "偶数" if is_even(num) else "奇数"
    print(f"{num}は{result}")

print_odd_or_even(args[1:len(args)])