class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(sub, i):
            if i == len(nums):
                res.append(sub[:])
                return

            sub.append(nums[i])
            dfs(sub, i + 1)

            sub.pop()
            j = i + 1
            while j < len(nums) and nums[j] == nums[i]:
                j += 1

            dfs(sub, j)

        dfs([], 0)
        return res