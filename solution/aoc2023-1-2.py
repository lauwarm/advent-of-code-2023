import re

def calculate_calibration_sum(calibration_document):
    total_sum = 0
    pattern = r"(\d)|(?=(one|two|three|four|five|six|seven|eight|nine))"

    for line in lines:
        digit_matches = re.findall(pattern, line, re.IGNORECASE)

        digits = []
        for match in digit_matches:
            if match[0]:
                digits.extend(map(int, str(match[0])))
            else:
                digits.append(english_to_digit(match[1]))

        first_digit = digits[0]
        last_digit = digits.pop()
        calibration_value = first_digit * 10 + last_digit
        total_sum += calibration_value

    return total_sum

def english_to_digit(word):
    # Map English words for digits to actual digits
    word_to_digit = {'one': 1, 
                     'two': 2, 
                     'three': 3, 
                     'four': 4, 
                     'five': 5, 
                     'six': 6, 
                     'seven': 7, 
                     'eight': 8, 
                     'nine': 9}
    return word_to_digit[word.lower()]

input_file_path = 'input/input-01'  # Update with the actual file path
with open(input_file_path, 'r') as file:
    lines = file.readlines()

result = calculate_calibration_sum(lines)
print("Sum of Calibration Values:", result)
