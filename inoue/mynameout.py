import sys

args = sys.argv
# 入力をstringへ変換
first_arg: str = args[1]

# -----------------------

def print_result(name: str):
    print(f"Hello {name} !")

# -----------------------

# 処理を実行する
def implement(arg):
    print_result(arg)

implement(first_arg)
