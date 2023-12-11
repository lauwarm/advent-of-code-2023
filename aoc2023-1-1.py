def calculate_sum_of_calibration_values(lines):
    # Initialize sum
    total_sum = 0
    
    # Iterate through each line
    for line in lines:
        # Extract calibration value for the current line
        calibration_value = extract_calibration_value(line)
        
        # Add to the total sum
        total_sum += calibration_value
    
    return total_sum

def extract_calibration_value(line):
    # Find the first digit in the line
    for char in line:
        if char.isdigit():
            first_digit = int(char)
            break
    else:
        # No digit found, handle this case (you can choose to return 0 or raise an exception)
        return 0
    
    # Find the last digit in the line
    for char in reversed(line):
        if char.isdigit():
            last_digit = int(char)
            break
    
    # Combine to form a two-digit number
    calibration_value = int(str(first_digit) + str(last_digit))
    
    return calibration_value

input_file_path = 'input/input-01-1'  # Update with the actual file path
with open(input_file_path, 'r') as file:
    lines = file.readlines()

# Example usage
#lines = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet", "nonnumeric"]
result = calculate_sum_of_calibration_values(lines)

# Print the result
print("Total Sum of Calibration Values:", result)