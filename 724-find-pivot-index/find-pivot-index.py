class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        prefixsum=[0]*len(nums)
        suffixsum=[0]*len(nums)
        
        sum=0

        for i in range(len(nums)):
            sum+=nums[i]

        suffixsum[0]=sum-nums[0]
        prefixsum[0]=0

        if (prefixsum[0]==suffixsum[0]):
            return 0
            
        for i in range(1,len(nums)):
            prefixsum[i]=prefixsum[i-1]+nums[i-1]
            suffixsum[i]=suffixsum[i-1]-nums[i]

            if(prefixsum[i]==suffixsum[i]):
                return i
        
        return -1
        