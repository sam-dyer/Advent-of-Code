# Puzzle 1 of day 3

with open("puzzle_input.txt") as file:
    input_file = file.readlines()



common_bit = 0
least_common_bit = 0
gamma_rate = ""
epsilon_rate = ""


for i in range(0, len(input_file[0])-1):
    zeros = 0
    ones = 0
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
    if ones > zeros:
        common_bit = 1
        least_common_bit = 0
    elif zeros > ones:
        common_bit = 0
        least_common_bit = 1
    
    gamma_rate = gamma_rate + str(common_bit)
    epsilon_rate = epsilon_rate + str(least_common_bit)

gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)

print(f"Power consumption: {gamma_rate * epsilon_rate}")