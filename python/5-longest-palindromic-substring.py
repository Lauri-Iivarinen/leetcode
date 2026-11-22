def longestPalindrome(self, s: str) -> str:
        
        def is_palin(s):
            # print("ispalin, ", s)
            if len(s) <= 1:
                return s
            l,r = 0,len(s) - 1
            ok = True
            while l < r:
                # print(s[l], s[r])
                if s[l] != s[r]:
                    return is_palin(s[:len(s)-1])
                l += 1
                r -= 1
            return s
        pals = []
        for i in range(len(s)):
            # print()
            # print("start iter ", s[i:])
            pals.append(is_palin(s[i:]))
        
        pals = sorted(pals,key=lambda x: len(x))


        # print(pals)
        return pals[-1]
