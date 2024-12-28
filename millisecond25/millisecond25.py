from dataclasses import dataclass
import string

@dataclass
class State:
  if_zero_write: int
  if_zero_move: int
  if_zero_next: string
  if_one_write: int
  if_one_move: int
  if_one_next: string

with open("input") as file:
  lines = file.read().splitlines()
  current_state = list(filter(lambda c: c.isupper(), lines[0]))[1]
  steps = int("".join(filter(lambda c: c.isnumeric(), lines[1])))

  states = {}

  for i in range(3, len(lines), 10):
    name = list(filter(lambda c: c.isupper(), lines[i]))[1]
    if_zero_write = int("".join(filter(lambda c: c.isnumeric(), lines[i+2])))
    if_zero_move = -1 if lines[i+3].find("left") > 0 else 1
    if_zero_next = list(filter(lambda c: c.isupper(), lines[i+4]))[1]
    if_one_write = int("".join(filter(lambda c: c.isnumeric(), lines[i+6])))
    if_one_move = -1 if lines[i+7].find("left") > 0 else 1
    if_one_next = list(filter(lambda c: c.isupper(), lines[i+8]))[1]

    states[name] = State(if_zero_write,if_zero_move,if_zero_next,if_one_write,if_one_move,if_one_next)

  tape = {}
  current_pos = 0

  for i in range(0,steps):
    if current_pos not in tape:
      tape[current_pos] = 0
    value = tape[current_pos]
    
    state = states[current_state]
    if value == 0:
      tape[current_pos] = state.if_zero_write
      current_pos += state.if_zero_move
      current_state = state.if_zero_next
    else:
      tape[current_pos] = state.if_one_write
      current_pos += state.if_one_move
      current_state = state.if_one_next

  print(sum(tape.values()))