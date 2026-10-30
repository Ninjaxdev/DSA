class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        hash={}
        low=0
        maxlen=0
        zerocount=0
        for high in range (len(nums)):
            if nums[high]==0:
                zerocount+=1
            
            while(zerocount > k):
                if nums[low] == 0:
                    zerocount -=1
                low+=1
            
            maxlen=max(maxlen,high-low+1)
        return maxlen
        