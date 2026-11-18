def the_shit_way_addBinary(self, a: str, b: str) -> str:
    # Self cooked method was too slow to pass and overflows
    def convert_num(s: list[str], t: list[str],c):
        if s == t:
            return c
        i = s.index("0")
        s[i] = "1"
        for j in range(0,i):
            s[j] = "0"
        c += 1
        return convert_num(s,t,c)

    def convert_binary(ta):
        bi = ["0"]
        for i in range(ta):
            if "0" not in bi:
                bi.append("0")
            bind = bi.index("0")

            bi[bind] = "1"
            for j in range(0,bind):
                bi[j] = "0"

        bi.reverse()
        return "".join(bi)

    #return convert_num("10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101")

    a_s = [v for v in a]
    a_t = ["0" for _ in a_s]
    a_n = convert_num(a_t, a_s[::-1], 0)

    b_s = [v for v in b]
    b_t = ["0" for _ in b_s]
    b_n = convert_num(b_t, b_s[::-1], 0)

    target = a_n + b_n
    return convert_binary(target)




def addBinary(self, a: str, b: str) -> str:
    import math
    def num_to_bin(n):
        if n == 0:
            return "0"
        s = ""
        m = 1
        i = math.floor(math.log2(n))
        for j in range(i+1):
            s = s + str((n // m) % 2)
            m = m * 2

        return s[::-1]

    def bin_to_num(b):
        m = len(b) - 1
        sm = 0
        for v in b:
            sm += int(v) * (2 ** m)
            m -= 1
        return sm

    return num_to_bin(bin_to_num(a) + bin_to_num(b))
    #print(num_to_bin(0))



print(addBinary(None, "0", "0"))


# 01000