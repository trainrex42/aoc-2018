#!/usr/bin/python3

import os

directory = os.path.dirname(os.path.realpath(__file__))

def reduce(poly):
  pointer = 0

  poly = list(poly)

  while pointer < (len(poly) - 1):
    l = poly[pointer]
    r = poly[pointer+1]

    if l != r and l.lower() == r.lower():
      poly.pop(pointer)
      poly.pop(pointer)
    
    else:
      pointer += 1
  
  return poly

def multiReduce(poly):
  new_poly = reduce(poly)

  while new_poly != poly:
    poly = new_poly[:]
    new_poly = reduce(poly)

  return poly

def part1():
  with open(directory + "/input") as f:
    data = f.readlines()

  poly = list(data[0].strip())

  poly = multiReduce(poly)
  
  return len(poly)

def part2():
  with open(directory + "/input") as f:
    data = f.readlines()

  poly = list(data[0].strip())

  units = []

  for c in poly:
    unit = {c.lower(),c.upper()}
    if unit not in units:
      units.append(unit)
  
  lens = dict()

  for unit in units:
    test_poly = [x for x in poly if x not in unit]

    rpoly = multiReduce(test_poly)

    lens[str(unit)] = len(rpoly)
  

  return lens[min(lens, key = lambda k: lens[k])]

def main():
  print("Part 1:", part1())
  print("Part 2:", part2())


if __name__ == "__main__":
  main()
