def intToRoman(self, num: int) -> str:
    m = num // 1000
    num -= 1000 * m
    d = num // 500
    num -= d * 500
    c = num // 100
    num -= 100 * c
    l = num // 50
    num -= 50 * l
    x = num // 10
    num -= x * 10
    v = num // 5
    num -= v * 5
    i = num // 1

    rom = ""
    rom += "M" * m
    if d + c == 5:
        rom += "CM"
    else:
        rom += "D" * d
        rom += "C" * c if c != 4 else "CD"
    if l + x == 5:
        rom += "XC"
    else:
        rom += "L" * l
        rom += "X" * x if x != 4 else "XL"
    if v + i == 5:
        rom += "IX"
    else:
        rom += "V" * v
        rom += "I" * i if i != 4 else "IV"

    return rom

print(intToRoman(None, 1994))
