def minChanges(self, s: str) -> int:
    def smallest_substring(divider, cap) -> int:
        if cap <= divider:
            return cap if cap < divider else divider
        if cap % divider == 0:
            return divider
        return smallest_substring(divider + 1, cap)

    smallest_set = smallest_substring(2, len(s))

    counter = 0

    while len(s) > 0:
        proc = s[:smallest_set]
        ones = proc.count("1")
        zeros = proc.count("0")

        if ones < zeros:
            counter += ones
        elif zeros < ones:
            counter += zeros
        elif zeros == ones and ones > 0:
            counter += ones
        
        s = s[smallest_set:]

    return counter




print(minChanges(None, "1001"))
#print(minChanges(None, "110"))
#print(minChanges(None, "11001"))
#print(minChanges(None, "110010000000000"))