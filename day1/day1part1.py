import re

sum_calibration_values = 0
for line in open('day1/trebuchet.txt').read().splitlines():
    digits = re.findall(r'\d', line)
    calibration_value = int(str(digits[0]) + str(digits[-1]))
    sum_calibration_values += calibration_value

print('Sum Calibration Value =', sum_calibration_values)
