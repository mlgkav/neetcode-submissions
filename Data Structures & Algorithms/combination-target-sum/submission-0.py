class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, combo, combo_sum):
            if combo_sum == target:
                res.append(combo[:])
                return
            if combo_sum > target or i >= len(nums):
                return
            
            # since a number can be used multiple times, we have the choice to stay at the same index 
            combo.append(nums[i])
            dfs(i, combo, combo_sum + nums[i])
            combo.pop()
            dfs(i + 1, combo, combo_sum)

        dfs(0, [], 0)
        
        return res