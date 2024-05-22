import sys

animals=["giraffe","tiger","zebra","elephant","lion"]
#第2引数で第3引数の動物名の挿入
args = sys.argv
num = args[1]
animal_name=args[2]
num=int(num)
 
animals.insert(num,animal_name)
 
#リストの数をカウント
count=len(animals)
del animals[count-1]
animals.sort(reverse=False)
print(animals,end="")