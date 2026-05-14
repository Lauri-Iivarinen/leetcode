#https://leetcode.com/problems/longest-substring-without-repeating-characters/
# should use set for optimal solution ig

class Solution:
    
    # the fast version
    def lengthOfLongestSubstring2(self, s: str) -> int:
        longest = 0
        queue = []
        for char in s:
            if char in queue:
                while queue[0] != char:
                    queue.pop(0)
                queue.pop(0)

            queue.append(char)

            if len(queue) > longest:
                longest = len(queue)
        
        return longest

    # the bruteforce shit version
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        values = {}
        curr = ""
        longest = ""
        while i < len(s):
            if s[i] in values:
                i = values[s[i]] + 1
                if len(curr) > len(longest):
                    longest = curr
                curr = ""
                values = {}
                continue

            curr += s[i]
            values[s[i]] = i
            i += 1
        
        if len(curr) > len(longest):
            longest = curr

        return len(longest)

test = Solution()

print(test.lengthOfLongestSubstring2("dvdff"))