with open("input") as f:
  data = [int(l) for l in f.readlines()]

print("Calculating Part 1")
print("Part 1:", sum(data))

f = 0
visited = []
i = 0

print("Calculating Part 2")

while f not in visited:
  visited.append(f)
  f += data[i]
  i = (i+1) % len(data)

print("Part 2:", f)



