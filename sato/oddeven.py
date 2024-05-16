import sys
args = sys.argv
num = args[1]
num=int(num)
#偶数か奇数か判定
if num % 2 == 0:
    print("偶数",end="")
else:
    print("奇数",end="")