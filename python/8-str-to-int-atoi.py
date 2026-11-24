import re
def myAtoi(self, s: str) -> int:
    if len(s) == 0:
        return 0
    nums = { "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9 }
    s = s.strip()
    mul = -1 if s.startswith("-") else 1
    #s = s.replace("-", "")
    #s = s.replace("+", "")
    s = re.sub(r"^[0+\-]*|[^\d].*","",s)

    m = len(s) - 1
    a = 0
    for v in s:
        if v not in nums:
            break
        tens = (10 ** m)
        if m == 0:
            tens = 1
        a += nums[v] * tens
        m -= 1
    ans = a * mul
    roof = 2 ** 31 -1
    floor = (roof + 1) * -1
    if ans > roof:
        ans = roof
    if ans < floor:
        ans = floor

    return ans


print(myAtoi(None, "-1337c0d3"))
print(myAtoi(None, " 0 "))
print(myAtoi(None, " +1"))
print(myAtoi(None, "24"))
print(myAtoi(None, "-543"))