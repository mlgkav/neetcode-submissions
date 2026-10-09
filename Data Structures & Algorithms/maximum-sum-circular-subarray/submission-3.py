class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # track the minimum subarray sum as well and then subtract that from the total sum 
        global_max = global_min = nums[0]
        min_start = 0
        curr_max = curr_min = nums[0]

        for i in range(1, len(nums)):
            curr_max = max(curr_max + nums[i], nums[i])
            curr_min = min(curr_min + nums[i], nums[i])
            global_max = max(global_max, curr_max)
            global_min = min(global_min, curr_min)
        
        return max(global_max, sum(nums) - global_min) if global_max > 0 else global_max