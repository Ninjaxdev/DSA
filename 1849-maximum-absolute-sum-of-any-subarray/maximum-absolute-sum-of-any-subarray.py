class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        b1=-math.inf
        b2=math.inf
        res1=0
        res2=0
        for i in range(len(nums)):
            b1=max(nums[i],b1+nums[i])
            res1=max(res1,b1)
            b2=min(nums[i],b2+nums[i])
            res2=min(res2,b2)
        return max(abs(res1),abs(res2))
        