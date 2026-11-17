class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum=0
        hashmap={0:1}
        count=0
        for num in nums:
            sum+=num
            q=sum-k
            count+=hashmap.get(q,0)
            hashmap[sum]=hashmap.get(sum,0)+1
        return count
            


        