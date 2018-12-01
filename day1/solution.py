#!/usr/bin/python3

def part1(directory):
  with open(directory + "input") as f:
    data = [int(l) for l in f.readlines()]

  return sum(data)

def part2(directory):
  with open(directory + "input") as f:
    data = [int(l) for l in f.readlines()]

  f = 0
  visited = set()
  i = 0
  while f not in visited:
    visited.add(f)
    f += data[i]
    i = (i+1) % len(data)

  return f



