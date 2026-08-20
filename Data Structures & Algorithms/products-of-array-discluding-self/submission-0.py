class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # left to right pass
        res = []
        left_prod = 1
        for n in nums:
            res.append(left_prod)
            left_prod *= n
        
        # right to left pass
        right_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right_prod
            right_prod *= nums[i]
        
        return res