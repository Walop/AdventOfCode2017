import time

def build_all_paths(current, components, path, paths):
  found = False
  for c in components:
    if c in path:
      continue
    if c[0] == current:
      found = True
      build_all_paths(c[1], components, path + [c], paths)
    if c[1] == current:
      found = True
      build_all_paths(c[0], components, path + [c], paths)
  if not found:
    paths.append(path)

with open("input") as file:
  components = [line.split("/") for line in file.read().splitlines()]
  for c in components:
    c[0]=int(c[0])
    c[1]=int(c[1])

  paths = []

  start = time.perf_counter()
  build_all_paths(0, components, [],paths)
  print("Built", len(paths), "paths in", time.perf_counter() - start, "seconds")

  longest = [[]]

  for path in paths:
    length = len(path)
    if length > len(longest[0]):
      longest = [path]
    elif length == len(longest[0]):
      longest.append(path)

  strongest = 0

  for path in longest:
    strength = sum(sum(component) for component in path)
    if strength > strongest:
      strongest = strength
  
  print(strongest)
