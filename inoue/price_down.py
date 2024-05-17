import sys
args = sys.argv

#引数を変数に代入
first_arg = args[1]
second_arg = args[2]

#品目（品名と価格）を辞書型で定義
hinmoku = {
  "リンゴ": 80,
  "みかん": 198,
  "バナナ": 150,
  "ビール": 360,
  "日本酒": 580,
  "ラーメン": 380,
  "うどん": 128,
  "パスタ": 258
}

fruits = ("リンゴ", "みかん", "バナナ")
alcohol = ("ビール", "日本酒")
noodles = ("ラーメン", "うどん", "パスタ")

#ここ以降にプログラムを書く

TYPE_MAP = {
  "麺類": noodles,
  "酒類": alcohol,
  "果物類": fruits,
}

def price_down(type, price):
  array = TYPE_MAP[type]
  for key in array:
    prevPrice = hinmoku[key]
    hinmoku[key] = prevPrice - price if prevPrice - price > 0 else 1
  print(hinmoku)

price_down(first_arg, int(second_arg))