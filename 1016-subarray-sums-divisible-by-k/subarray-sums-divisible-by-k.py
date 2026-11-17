class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        sum=0
        hashmap={0:1}
        count=0
        for num in nums:
            sum+=num
            rem=sum%k
            if rem<0:
                rem=rem+k
            count+=hashmap.get(rem,0)
            hashmap[rem]=hashmap.get(rem,0)+1
            
        return count
        