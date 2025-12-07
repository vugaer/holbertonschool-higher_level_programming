def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0
    i = 0

    while i < len(roman_string):
        current_val = roman_map.get(roman_string[i], 0)
        next_val = roman_map.get(roman_string[i + 1], 0) if i + 1 < len(
            roman_string) else 0

        if current_val < next_val:
            result += next_val - current_val
            i += 2
        else:
            result += current_val
            i += 1

    return result
