class ProductOfNumbers:
    
    def __init__(self):
        self.nums = []
        self.mul = {}

    #[2,2,4,3]
    #{1:2, 2: 4, 3: 16, 4: 48}
    # get 1 = x[4] / x[3] -> 48 / 16 = 3
    # get 2 = x[4] / x[2] -> 48 / 4
    # what about 0

    def add(self, num: int) -> None:
        self.nums.append(num) # cant think of way to check for 0 in O(1)
        #print(self.nums)
        if num == 0:
            num = 1
        if len(self.nums) == 1:
            self.mul[1] = num
        else:
            self.mul[len(self.nums)] = self.mul[len(self.nums) - 1] * num

    def getProduct(self, k: int) -> int:
        #print(k, self.nums)
        if 0 in self.nums[len(self.nums) - k:]:
            return 0
        v1 = self.mul[len(self.nums)]
        v2 = self.mul[len(self.nums) - k] if len(self.nums) - k in self.mul else 1
        return int(v1 / v2) if v1 != 0 and v2 != 0 else 0