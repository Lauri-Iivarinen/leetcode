def isPalindrome(self, s: str) -> bool:
        abc = set(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])
        
        s = s.lower()
        palindrome = ""
        for c in s:
            if c in abc:
                palindrome += c
        # 3 // 2 = 1
        # 4 // 2 = 2
        r = len(palindrome) // 2
        l = r - 1
        if len(palindrome) % 2 != 0:
            r += 1
        
        while l >= 0:
            if palindrome[l] != palindrome[r]:
                return False
            l -= 1
            r += 1
        
        return True
