def is_game_possible(game, red_limit, green_limit, blue_limit):
    red_count = 0
    green_count = 0
    blue_count = 0

    for subset in game:
        for cube in subset.split(", "):
            count, color = cube.split()
            count = int(count)
            
            # Check the color and update the corresponding count
            if color == "red":
                red_count += count
                if red_count > red_limit:
                    return False
                else:
                    red_count = 0
            elif color == "green":
                green_count += count
                if green_count > green_limit:
                    return False
                else:
                    green_count = 0
            elif color == "blue":
                blue_count += count
                if blue_count > blue_limit:
                    return False
                else:
                    blue_count = 0

    return True

def sum_of_possible_game_ids(games, red_limit, green_limit, blue_limit):
    possible_games = [int(game.split(":")[0].split()[1]) for game in games if is_game_possible(game.split(":")[1].strip().split(";"), red_limit, green_limit, blue_limit)]
    return sum(possible_games)

# Specify cube limits
red_limit = 12
green_limit = 13
blue_limit = 14

input_file_path = 'input/input-02'  # Update with the actual file path
with open(input_file_path, 'r') as file:
    lines = file.readlines()

# Calculate the sum of IDs of possible games
result = sum_of_possible_game_ids(lines, red_limit, green_limit, blue_limit)
print(result)