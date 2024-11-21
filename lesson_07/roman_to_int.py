def roman_to_integer(roman: str) -> int:
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    for i in range(len(roman) - 1):
        if roman_dict[roman[i]] < roman_dict[roman[i + 1]]:
            total -= roman_dict[roman[i]]
        else:
            total += roman_dict[roman[i]]
    return total + roman_dict[roman[-1]]


if __name__ == "__main__":
    print(roman_to_integer("LVIII"))
    print(roman_to_integer("MMXXIV"))
