import sys
args = sys.argv

#引数を変数に代入
first_arg = args[1]
second_arg = args[2]

#品目（品名と価格）を辞書型で定義
ITEM_PRICE = {
  "リンゴ": 80,
  "みかん": 198,
  "バナナ": 150,
  "ビール": 360,
  "日本酒": 580,
  "ラーメン": 380,
  "うどん": 128,
  "パスタ": 258
}

FRUITS = ("リンゴ", "みかん", "バナナ")
ALCOHOL = ("ビール", "日本酒")
NOODLES = ("ラーメン", "うどん", "パスタ")

#ここ以降にプログラムを書く

TYPE_MAP = {
  "麺類": NOODLES,
  "酒類": ALCOHOL,
  "果物類": FRUITS,
}

def price_down(type, price_reduction_amount):
  items = TYPE_MAP[type]
  for key in items:
    prevPrice = ITEM_PRICE[key]
    ITEM_PRICE[key] = prevPrice - price_reduction_amount if prevPrice - price_reduction_amount > 0 else 1
  print(ITEM_PRICE)

price_down(first_arg, int(second_arg))