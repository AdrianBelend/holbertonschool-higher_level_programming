#!/usr/bin/python3
def roman_to_int(roman_string):
    rd = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string is None or type(roman_string) is not str:
        return 0
    sum = 0
    for i in range(len(roman_string)):
        if i > 0 and rd[roman_string[i]] > rd[roman_string[i - 1]]:
            sum += rd[roman_string[i]] - 2 * rd[roman_string[i - 1]]
        else:
            sum += rd[roman_string[i]]
    return sum
