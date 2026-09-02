class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # for each num, it can either be part of the sequence or not part of the sequence
        res = []
        def dfs(i, subset):
            if i >= len(nums):
                res.append(subset[:])
                return

            subset.append(nums[i])
            dfs(i + 1, subset)
            subset.pop()
            dfs(i + 1, subset)
        dfs(0, [])
        return res