import sys

args = sys.argv
first_arg = int(args[1]) # index
second_arg = args[2] # 動物名

animals = ["giraffe", "tiger", "zebra", "elephant", "lion"]

def insert_elm(index, animalName):
  animals.insert(index, animalName)

def delete_last_elm():
  animals.pop(-1)

def sort_in_ascending_order():
  animals.sort()

insert_elm(first_arg, second_arg)
delete_last_elm()
sort_in_ascending_order()

print(animals)