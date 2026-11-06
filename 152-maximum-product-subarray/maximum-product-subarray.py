class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        minending=nums[0]
        maxending=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            v1=minending*nums[i]
            v3=maxending*nums[i]
            v2=nums[i]
            minending=min(v2,min(v1,v3))
            maxending=max(v2,max(v1,v3))
            ans=max(ans,max(minending,maxending))
        return ans

        