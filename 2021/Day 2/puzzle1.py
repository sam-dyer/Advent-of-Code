# Puzzle 1 of day 2

with open("puzzle_input.txt") as file:
    input_file = file.readlines()

horizontal_pos = 0
depth = 0

for i in range(0, len(input_file)):
    direction, value = input_file[i].split(' ')
    value = int(value)
    if direction == "forward":
        horizontal_pos += value
    elif direction == "down":
        depth += value
    elif direction == "up":
        depth -= value

print(f"Result: {horizontal_pos * depth}")
