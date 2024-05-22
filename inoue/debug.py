
#第2引数でインデックスの位置、第3引数の動物名の挿入
import sys
args = sys.argv
num = args[1]
animal_name=args[2]
 
#引き数を整数型に直す
num=int(num)
 
#指定位置に要素を挿入
animals.insert(num,animal_name)
 
#リストの要素数をカウント
count=len(animals)
 
#リストの最後の要素を削除
del animals[count-1]
 
#逆順に並べる
animals.sort(reverse=False)