class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_i_minus_1 = rob_i_minus_2 = 0
        for n in nums:
            rob_i_minus_1, rob_i_minus_2 = max(rob_i_minus_1, rob_i_minus_2 + n), rob_i_minus_1
        
        return rob_i_minus_1