class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        #arr1.sort()
        arr2.sort()

        def find_if_range(v, d, arr, l, r):
            m = (r + l) // 2
            # print(l,m,r)
            if r - l <= 1:
                return (arr[l] >= v - d and arr[l] <= v + d) or (arr[r] >= v - d and arr[r] <= v + d)
            if arr[m] >= v - d and arr[m] <= v + d:
                return True 

            if arr[m] < v:
                return find_if_range(v, d, arr, m, r)
            else:
                return find_if_range(v, d, arr, l, m)

        
        ans = 0
        for v in arr1:
            l = 0
            r = len(arr2) - 1
            # print("find ", v)
            f = find_if_range(v, d, arr2, l, r)
            #print(f)
            if not f:
                ans += 1



        return ans
