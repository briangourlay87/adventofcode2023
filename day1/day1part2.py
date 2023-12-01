import re

numbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

sum_calibration_values = 0
for line in open('day1/trebuchet.txt').read().splitlines():
    digits = re.findall(r"(?=(\d|" + '|'.join(numbers.keys()) + "))", line)
    first_digit = str(digits[0]) if digits[0].isnumeric() else numbers.get(digits[0])
    last_digit = str(digits[-1]) if digits[-1].isnumeric() else numbers.get(digits[-1])
    calibration_value = int(first_digit + last_digit)
    sum_calibration_values += calibration_value

print('Sum Calibration Value =', sum_calibration_values)
