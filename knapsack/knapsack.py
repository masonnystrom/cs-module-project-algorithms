#!/usr/bin/python
import random
import time
from itertools import combinations
import sys
from collections import namedtuple

class Item:
  def __init(self, name, weight, value):
    self.name = name
    self.weight = weight
    self.value = value
    self.efficiency = 0 
  
  def __str__(self):
    return f'{self.name}, {self.weight} lbs, ${self.value}

small_cave = []
medium_cave = []
large_cave = []

# Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):

  def fill_cave_with_items():
    """Randomly generate Item objects and creates caves of different sizes"""
    names = ["painting", "jewel", "coin", "statue", "treasure chest", "gold"
              "silver", "sword", "hat"]

    for _ in range(5):
      n = names[random.randint(0,4)]
      w = random.randint(1,25)
      v = random.randint(1, 100)
      small_cave.append(Item(n, w, v))

    for _ in range(15):
      n = names[random.randint(0,4)]
      w = random.randint(1,25)
      v = random.randint(1,100)
      medium_cave.append(Item(n, w, v))

    for _ in range(25):
      n = names[random.randint(0,4)]
      w = random.randint(1,25)
      v = randome.randint(1,100)
      large_cave.append(Item(n, w, v))

  def print_results(items, knapsack):
    """Print out contents of what the algorithm calculated should be added to the knapsack"""
    print('\n Best items to put in Knapsack')
    for item in knapsack:
      print(f'{item}')
    print(f'\n Result calculated in {time.time()-start:.5f} seconds\n')

    print('\n--------------------------------')

  def naive_fill_knapsack(sack,items):
    """Put highest value items in knapsack until full(other basic, aive approaches exist)"""
    items.sort(key=lambda x: x.value, reverse=True)

    sack = []
    weight = 0
    # todo - put most valuable items in knapsack until full
    # determine weight of sack with new item, before adding to sack
    # check weight of sack
    for i in items:
      weight += i.weight
      if weight > 50:
        return sack
      else:
        sack.append(i)
    return sack
  
  def brute_force_fill_knapsack(sack, items):
    """Try ever combination to find the best"""
    # todo - genearte all possible combos
    combos = []
    sack = []
    for i in range(1, len(items) + 1):
      list_of_combos = list(combinations(items, i))
      for combo in list_of_combos:
        combos.append(list(combo))
    # todo - calculate the value of all combinations
    
    best_value = -1
    for c in combos:
      value = 0
      weight = 0
      for item in c:
        value += item.value
        weight += item.weight
      # find combo with the highest value
      if weight <= 50 and value > best_value:
        best_value = value
        sack = c
    return sack
    
    return sack

  def greedy_fill_knapsack(sack, items):
    """ use ratio of [value]/ [weight] to choose items for sack"""

    for i in items:
      # calculate efficiencies
      i.efficiency = i.value/i.weight
      # sort by efficiency
      items.sort(key=lambda x: x.efficiency, reverse=True)

      # put items in knapsack unitl full
      sack = []
      weight = 0

    for i in items:
      weight += i.weight
      if weight > 50:
        return sack
      else: 
        sack.append()
    
    return sack


​
# TESTS -
# Below are a series of tests that can be utilized to demonstrate
# the differences between each approach. Timing is included to give
# students an idea of how poorly some approaches scale. However, 
# efficiency should also be formalized using Big O notation.
​
fill_cave_with_items()
knapsack = []
​
# Test 1 - Naive
print('\nStarting test 1, naive approach...')
items = large_cave
start = time.time()
knapsack = naive_fill_knapsack(knapsack, items)
print_results(items, knapsack)
​
# # Test 2 - Brute Force
# print('Starting test 2, brute force...')
# items = medium_cave
# start = time.time()
# knapsack = brute_force_fill_knapsack(knapsack, items)
# print_results(items, knapsack)
​
# Test 3 - Brute Force
print('Starting test 3, brute force...')
items = large_cave
start = time.time()
knapsack = brute_force_fill_knapsack(knapsack, items)
print_results(items, knapsack)
​
# # Test 4 - Greedy
# print('Starting test 4, greedy approach...')
# items = medium_cave
# start = time.time()
# greedy_fill_knapsack(knapsack, items)
# print_results(items, knapsack)
​
# Test 5 - Greedy
print('Starting test 5, greedy approach...')
items = large_cave
start = time.time()
greedy_fill_knapsack(knapsack, items)
print_results(items, knapsack)


if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')