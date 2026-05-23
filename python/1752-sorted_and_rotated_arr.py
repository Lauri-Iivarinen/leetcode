class Solution:
    def check(self, nums: list[int]) -> bool:
        prev_num = nums[0]
        rotated = False

        for num in nums:
            if num < prev_num:
                if not rotated:
                    rotated = True
                else:
                    return False
            prev_num = num
        
        return not rotated or nums[0] >= nums[-1]