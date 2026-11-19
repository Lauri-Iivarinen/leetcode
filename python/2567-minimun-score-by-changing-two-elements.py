class Solution:
    def minimizeSum(self, nums: list[int]) -> int:
        nums.sort()
        return min( nums[-1] - nums[2], nums[-2] - nums[1], nums[-3] - nums[0] )

    # since im stupid I always tend to brute force the first answer without thinking
    def minimizeSumSLOW(self, nums: list[int]) -> int:
        # 1. search for max, change val so max is 2nd highest
        # 2. then eliminate min val
        sums = {}
        i = 0
        j = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j == i:
                    continue
                sm = abs(nums[i] - nums[j])
                if (j,i) not in sums:
                    sums[i,j] = (sm,nums[i],i,nums[j],j)
        
        sums = sorted(sums.values(), key=lambda x : x[0])

        # Eliminate the 2 smallest numbers that cause the highest caps
        # OR eliminate 2 largest ?
        # OR eliminate largest then smallest
        # OR eliminate smallest into largest
        # account for min sums as well
        

        def proc(sums, f1, f2):
            mn = (sums[-1][1], sums[-1][2]) if f1(sums[-1][1], sums[-1][3]) else (sums[-1][3], sums[-1][4])
            sums = list(filter(lambda x: x[2] != mn[1] and x[4] != mn[1], sums))
            mn = (sums[-1][1], sums[-1][2]) if f2(sums[-1][1], sums[-1][3]) else (sums[-1][3], sums[-1][4])
            sums = list(filter(lambda x: x[2] != mn[1] and x[4] != mn[1], sums))
            return sums[-1][0] if len(sums) > 0 else 0

        # greater
        def g(a,b):
            return a > b
        
        # less
        def l(a,b):
            return a < b
        #z = zi(sums)

        _ss = proc(sums,l,l) # SmallSmall
        _ll = proc(sums,g,g) # LargeLarge
        _ls = proc(sums,g,l)
        _sl = proc(sums,l,g)

        print([_ss,_ll,_ls,_sl])

        return min([_ss,_ll,_ls,_sl])
        