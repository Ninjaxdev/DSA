class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        curr_max = curr_min = nums[0]
        max_sum = min_sum = nums[0]
        total_sum = nums[0]
        
        for i in range(1, len(nums)):
            total_sum += nums[i]
            
            # 2. Track current max and current min separately
            curr_max = max(curr_max + nums[i], nums[i])
            curr_min = min(curr_min + nums[i], nums[i])
            
            # Update global max and global min
            max_sum = max(max_sum, curr_max)
            min_sum = min(min_sum, curr_min)
            
        # 3. Handle the all-negative edge case
        if max_sum < 0:
            return max_sum
            
        # 4. Subtract the global min_sum from total_sum for the circular case
        return max(max_sum, total_sum - min_sum)
            
        
        