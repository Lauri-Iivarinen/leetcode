def threeSum(self, nums: list[int]) -> list[list[int]]:
        mp = {}
        for i in range(len(nums)):
            if nums[i] in mp:
                mp[nums[i]] += 1
            else:
                mp[nums[i]] = 1

        ans = []
        ans_k = set()

        def save(n_i,n_k,n_j):
            pot = [n_i,n_k,n_j]
            pot.sort()
            p = [str(v) for v in pot]
            if ".".join(p) not in ans_k:
                ans_k.add(".".join(p))
                ans.append(pot)
                

        for n_i in mp.keys():
            for n in mp.keys():
                c = 0 - n_i - n
                if c in mp:
                    if c == n or c == n_i or n == n_i:
                        if n_i == n and c == n and mp[c] >= 3:
                            save(n_i,n, c)
                        elif n_i == n and c != n and mp[n] >= 2:
                            save(n_i,n, c)
                        elif n_i != n and c == n and mp[n] >= 2:
                            save(n_i,n, c)
                        elif n_i == c and c != n and mp[c] >= 2:
                            save(n_i,n, c)
                    else:
                        save(n_i,n, c)

        return ans