def lengthOfLastWord(self, s: str) -> int:
        import re
        return len(re.sub("^.* ", "", s.strip()))

print(lengthOfLastWord(None, ""))
print(lengthOfLastWord(None, "a"))
print(lengthOfLastWord(None, " a "))
print(lengthOfLastWord(None, " ab"))
print(lengthOfLastWord(None, " a ab"))