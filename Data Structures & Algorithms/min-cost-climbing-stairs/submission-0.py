class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost_i_minus_1 = min_cost_i_minus_2 = 0
        for i in range(2, len(cost) + 1):
            min_cost_i_minus_1, min_cost_i_minus_2 = min(min_cost_i_minus_1 + cost[i - 1], min_cost_i_minus_2 + cost[i - 2]), min_cost_i_minus_1
        return min_cost_i_minus_1
