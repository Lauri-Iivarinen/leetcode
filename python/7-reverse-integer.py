def reverse(self, x: int) -> int:
        negation = ""
        x = str(x)

        if x.startswith("-"):
            negation = "-"
            x = x[1:]
        
        v = negation + x[::-1]

        v = int(v)
        if v >= 2 ** 31 or v < (2 ** 31) * -1:
            return 0
        
        return v
