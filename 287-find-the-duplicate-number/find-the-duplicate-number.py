class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # for slow in range(len(nums)):
        #     f=slow+1
        #     while(f<len(nums)):
        #         if nums[slow] ^ nums[f]:
        #             f+=1
        #         else:
        #             return nums[f]

        slow=0
        fast=0
        while(True):
            slow=nums[slow]
            fast=nums[fast]
            fast=nums[fast]
            if slow==fast:
                slow=0
                while(slow!=fast):
                    slow=nums[slow]
                    fast=nums[fast]
                return fast



        