class NumArray:

    def __init__(self, nums: list[int]):
        if not nums:
            self.lum = []
            return
            
        self.lum = [0] * len(nums)
        self.lum[0] = nums[0]
        for i in range(1, len(nums)):
            self.lum[i] = self.lum[i - 1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left==0 :
            return self.lum[right]
        
        return (self.lum[right]-self.lum[left-1])
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)