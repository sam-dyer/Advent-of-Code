# Puzzle 2 of day 1

with open("puzzle_input.txt") as file:
    input_file = file.readlines()

previous_sum = "NONE"
increaced = 0

for i in range(0, len(input_file)):
    try:
        current_sum = int(input_file[i]) + int(input_file[i +1]) + int(input_file[i + 2])
    except:
        pass
    if previous_sum == "NONE":
        print(f"{current_sum} no previous sum")
    elif previous_sum < current_sum:
        increaced += 1
        print(f"{current_sum} Increaced")
    elif previous_sum > current_sum:
        print(f"{current_sum} Decreaced") 

    previous_sum = current_sum

print(f"Total increaced sums: {increaced}")