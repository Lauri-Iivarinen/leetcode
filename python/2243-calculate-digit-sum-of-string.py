import re
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        t = []
        while len(s) > k:
            t = []
            e = s[-1 * (len(s) % k):] if len(s) % k > 0 else ""
            r = ".{}{}{}".format("{", k, "}")
            strings = re.findall(r, s)
            if len(e) > 0:
                strings += [e]
            print(strings)
            sm = 0
            for string in strings:
                m = [int(v) for v in string]
                t.append(str(sum(m)))
            s = "".join(t)
        return s