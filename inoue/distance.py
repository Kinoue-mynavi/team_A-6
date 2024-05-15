import sys
import math

first_arg = sys.argv[1]
second_arg = sys.argv[2]

DISTANCE = {
  "東京": 0.00,
  "品川": 6.78,
  "新横浜": 25.54,
  "名古屋": 342.02,
  "京都": 476.31,
  "新大阪": 515.35,
}

def print_distance():
    if first_arg and second_arg:
      result = round(DISTANCE[first_arg] - DISTANCE[second_arg], 2)if  DISTANCE[first_arg] > DISTANCE[second_arg] else round(DISTANCE[second_arg] - DISTANCE[first_arg], 2)
      return result
    else:
      return "Error: Please enter the first and second arguments"

print(print_distance())