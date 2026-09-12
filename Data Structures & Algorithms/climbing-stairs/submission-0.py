class Solution:
    def climbStairs(self, n: int) -> int:
        ways_n, ways_n_minus_1 = 1, 0
        for _ in range(n):
            ways_n_minus_1, ways_n = ways_n, ways_n + ways_n_minus_1
        
        return ways_n