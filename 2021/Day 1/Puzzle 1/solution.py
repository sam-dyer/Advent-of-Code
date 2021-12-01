# Puzzle 1 of day 1

with open("puzzle_input.txt") as file:
    input_file = file.readlines()

increaced = 0
previous_depth = "NONE"

for i in range(0, len(input_file)):
    current_depth = int(input_file[i])
    if previous_depth == "NONE":
        print(f"{current_depth} no previous measurment")
    elif previous_depth < current_depth:
        increaced += 1
        print(f"{current_depth} Increaced")
    elif previous_depth > current_depth:
        print(f"{current_depth} Decreaced") 

    previous_depth = current_depth
        
print(f"Measurements larger than previous: {increaced}")
        