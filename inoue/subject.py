import sys

args = sys.argv
first_arg = int(args[1])
second_arg = int(args[2])
third_arg = int(args[3])

# -----------------------

def calc(arg1, arg2, arg3):
    sum = arg1 + arg2 + arg3
    if (sum >= 220 and (arg1 >= 70 and arg2 >= 70 and arg3 >= 70)):
        print("合格")
        return
    
    print("不合格")

# -----------------------

# 処理を実行する

calc(first_arg, second_arg, third_arg)