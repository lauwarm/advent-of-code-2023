def calculate_minimum_set(game):
    sum_power = 0
    min_red = 0
    min_green = 0
    min_blue = 0

    for subset in game:
        for cube in subset.split(", "):
            count, color = cube.split()
            count = int(count)

            if color == "red" and count > min_red:
                min_red = count
            elif color == "green" and count > min_green:
                min_green = count
            elif color == "blue" and count > min_blue:
                min_blue = count

    sum_power += min_red * min_green * min_blue
    #return min_red * min_green * min_blue
    return sum_power

def sum_of_minimum_set_powers(games):
    return sum(calculate_minimum_set(game.split(":")[1].strip().split(";")) for game in games)

input_file_path = 'input/input-02'  # Update with the actual file path
with open(input_file_path, 'r') as file:
    lines = file.readlines()

# Calculate the sum of powers of minimum sets
result = sum_of_minimum_set_powers(lines)
print(result)
