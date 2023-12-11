# not done
import re

def calculate_calibration_sum(calibration_document):
    total_sum = 0

    # Find all English words for digits and numeric digits using regular expression
    digit_matches = re.findall(r'\b(\d+)|(one|two|three|four|five|six|seven|eight|nine)\b', calibration_document, re.IGNORECASE)

    digits = []
    for match in digit_matches:
        if match[0]:
            digits.extend(map(int, str(match[0])))
        else:
            digits.append(english_to_digit(match[1]))

    # Combine first and last digits for each pair
    for i in range(0, len(digits), 2):
        first_digit = digits[i]
        last_digit = digits[i + 1] if i + 1 < len(digits) else 0

        calibration_value = first_digit * 10 + last_digit
        total_sum += calibration_value

    return total_sum

def english_to_digit(word):
    # Map English words for digits to actual digits
    word_to_digit = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    return word_to_digit[word.lower()]

# Example usage
calibration_document = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

result = calculate_calibration_sum(calibration_document)
print("Sum of Calibration Values:", result)
