import math

def is_power_of_ten(number):
    return math.log10(number)%1==0

number_to_check = 1000
if is_power_of_ten(number_to_check):
    print("number is power of ten:",number_to_check)
else:
    print("number is not power of ten:",number_to_check)