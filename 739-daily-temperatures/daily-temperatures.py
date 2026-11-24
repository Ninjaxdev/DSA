class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans=[0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)-1,-1,-1):
            while(stack and temperatures[i]>=temperatures[stack[-1]]):
                stack.pop()
            
            if stack:
                ans[i]=stack[-1]-i
            
            stack.append(i)
        
        return ans
        
        