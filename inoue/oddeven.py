import sys

args = sys.argv
# 入力をintegerへ変換
first_arg: int = int(args[1])

# -----------------------

# 偶数か奇数かを判定する
def is_even(num: int) -> bool:
    return num % 2 == 0

def print_result(num):
    if (is_even(num)):
        print("偶数")
    else:
        print("奇数")

# -----------------------

# 処理を実行する
def implement(arg):
    print_result(arg)

implement(first_arg)