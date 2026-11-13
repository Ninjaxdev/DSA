class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        lum=[0]*len(nums)
        low=0
        lum[low]=nums[low]
        for i in range(1,len(nums)):
            lum[i]=lum[i-1]+nums[i]
        return lum
        