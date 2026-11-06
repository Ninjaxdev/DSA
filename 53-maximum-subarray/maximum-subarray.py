class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        bestending=-math.inf
        ans=-math.inf
        for i in range(len(nums)):
            v1=bestending+nums[i]
            v2=nums[i]
            bestending=max(v1,v2)
            ans=max(bestending,ans)
        return ans