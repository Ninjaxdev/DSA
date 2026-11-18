class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        one=0
        zero=0
        res=0
        hashmap={}
        for i in range(len(nums)):
            if nums[i]==0:
                zero+=1
            else:
                one+=1
            diff=zero-one
            if diff==0:
                res=max(res,i+1)
                continue
            if diff in hashmap: # check if diff exist in hashmap
                length=i-hashmap[diff]
                res=max(res,length)
            else: #if we did not see the diff then store it in hashmap
                hashmap[diff]=i
        return res

        