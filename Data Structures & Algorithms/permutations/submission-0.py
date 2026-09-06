class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        picked_nums = [False] * len(nums)
        def dfs(permutation):
            if len(permutation) == len(nums):
                res.append(permutation[:])
                return

            for i, picked in enumerate(picked_nums):
                if not picked:
                    permutation.append(nums[i])
                    picked_nums[i] = True
                    dfs(permutation)
                    permutation.pop()
                    picked_nums[i] = False

        dfs([])
        return res
