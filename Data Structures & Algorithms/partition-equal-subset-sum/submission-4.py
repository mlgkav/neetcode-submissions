class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        
        target = total // 2
        
        dp = [False] * (target + 1)
        dp[0] = True

        for n in nums:
            for i in range(target, n - 1, -1):
                dp[i] = dp[i - n] or dp[i]
            # Short circuit
            if dp[-1]:
                return True
            
        return dp[-1]