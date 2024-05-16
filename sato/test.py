import sys
args = sys.argv
#点数の入力
math = args[1]
jap = args[2]
eng = args[3]

math = int(math)
jap = int(jap)
eng = int(eng)
#3教科合計
sum=math+jap+eng
#合否判定
is_check =(((math>=70)and(jap>=70)and(eng>=70))or(sum>=220))and((math>=50)and(jap>=50)and(eng>=50))
if is_check:
    print("合格",end="")
else:
    print("不合格",end="")