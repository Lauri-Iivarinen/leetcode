def maxLength(self, nums: list[int]) -> int:

        def lcm(vals, curr, mx):
            for n in vals:
                if curr % n != 0:
                    return lcm(vals, curr+mx, mx)
            return curr

        def gcd(vals, curr):
            if curr <= 1:
                return 1
            for v in vals:
                if v % curr != 0:
                    curr -= 1
                    return gcd(vals, curr)
            return curr
       
        ans = 0
        for i in range(len(nums)):
            n = 1
            for j in range(i+1,len(nums)+1):
                
                #st = set(nums[i:j])
                l = nums[i:j]
                n = n * nums[j-1]
                mx = max(l)
               
                _lcm = lcm(l, mx, mx)
                _gcd = gcd(l, mx)

                if n == _gcd * _lcm and len(l) > ans:
                    ans = len(l)

        return ans

# this timeouts -> optimize
#print(maxLength(None, [1,2,1,2,1,1,1]))
print(maxLength(None, [10,4,2,7,8,7,2,8,2,10,5,6,9,6,10,2,2,2,6,6,1,9,3,7,10,4,5,6,5,2,7,1,4,1,1,4,1,10,3,3,1,9,10,10,2,1,6,2,9,7,3,6,2,9,8,2,10,6,9,4,1,9,7,10,3,9,1,10,10,7,9,5,10,10,4,10,1,8,2,1,9,5,4,7,7,2,1,7,1,1,10,7,3,10,9,2,6,10,9,5]))