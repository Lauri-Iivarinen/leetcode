class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        v = 10 ** 10
        f = False
        for i in range(len(nums) - l + 1):
            for j in range(l,r+1):
                s = sum(nums[i:i+j])
                #print(i,i+j,s)
                if s < v and s > 0 and len(nums[i:i+j]) >= l:
                    #print("smaller")
                    f = True
                    v = s
        
        return v if f else -1