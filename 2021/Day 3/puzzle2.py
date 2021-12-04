# Puzzle 2 of day 3

with open("puzzle_input.txt") as file:
    input_file = file.readlines()



common_bit = 0
least_common_bit = 0
oxygen_rating = ""

# Oxygen generator

for i in range(0, len(input_file[0])-1):
    if len(input_file) == 1:
        break
    zeros = 0
    ones = 0
    j = 0
    for j in range(0, len(input_file)):
        try:
            bit = input_file[j]
            bit = str(bit)[i]
        except:
            break
        if bit == '1':
            ones += 1
        elif bit == '0':
            zeros += 1
        else:
            break
    if zeros > ones:
        common_bit = 0
    elif ones > zeros:
        common_bit = 1
    temp_list = []
    k = 0
    for k in range(0, len(input_file)):
        if (input_file[k][i]) == str(common_bit):
            temp_list.append(input_file[k])
    input_file = temp_list
oxygen_rating = (int(input_file[0], 2))



with open("puzzle_input.txt") as file:
    input_file = file.readlines()



# CO2 Scrubber

co2_rating = ""

for i in range(0, len(input_file[0])-1):
    if len(input_file) == 1:
        break
    zeros = 0
    ones = 0
    j = 0
    for j in range(0, len(input_file)):
        try:
            bit = input_file[j]
            bit = str(bit)[i]
        except:
            break
        if bit == '1':
            ones += 1
        elif bit == '0':
            zeros += 1
        else:
            break
    if zeros < ones:
        least_common_bit = 0
    elif ones < zeros:
        least_common_bit = 1
    
    temp_list = []
    k = 0
    for k in range(0, len(input_file)):
        if (input_file[k][i]) == str(least_common_bit):
            temp_list.append(input_file[k])
    input_file = temp_list
co2_rating = (int(input_file[0], 2))


print(f"Life support rating: {co2_rating * oxygen_rating}")