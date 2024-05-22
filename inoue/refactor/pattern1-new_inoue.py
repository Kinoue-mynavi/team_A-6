import sys

args = sys.argv
first_arg = int(args[1]) # index
second_arg = args[2] # 動物名

ANIMALS = ["giraffe", "tiger", "zebra", "elephant", "lion"]

def insert_animal(index, animalName):
  ANIMALS.insert(index, animalName)

def delete_last_animal():
  ANIMALS.pop(-1)

def sort_in_ascending_order():
  ANIMALS.sort()

insert_animal(first_arg, second_arg)
delete_last_animal()
sort_in_ascending_order()

print(ANIMALS)