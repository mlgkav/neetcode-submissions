class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_1 = rob_2 = 0
        for n in nums:
            rob_1, rob_2 = max(rob_1, rob_2 + n), rob_1
        
        return rob_1