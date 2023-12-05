from collections import Counter

def first_non_repeating_char(input_string):
    char_count = Counter(input_string)

    for char in input_string:
        if char_count[char] == 1:
            return char

    return None
input_str = "abababcdabababcabc"
result = first_non_repeating_char(input_str)
if result:
    print("the first non repeating charecter is:",result)
else:
    print("no non repeating charecter found")