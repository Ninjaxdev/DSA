class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        low=0
        high=len(nums)-1
        start=-1
        last=-1
        while(low<=high):
            mid=low+(high-low)//2
            if(nums[mid]==target):
                start=mid
                high=mid-1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        
        if start==-1:
            return [start,last]
        
        low=0
        high=len(nums)-1

        while(low<=high):
            mid=low+(high-low)//2
            if(nums[mid]==target):
                last=mid
                low=mid+1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1

        
        return [start,last]