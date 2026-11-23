class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n=len(nums)
        res=[-1]*n
        stack=[]
        stack.append(nums[n-1])
        for i in range(2*n-1,-1,-1):
            curr=nums[i%n]
            while(stack and stack[-1]<=curr):
                stack.pop()
            if i<n :
                if stack:
                    res[i]=stack[-1]
            
            stack.append(curr)
        return res