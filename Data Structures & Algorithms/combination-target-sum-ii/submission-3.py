class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(start, combo, total):
            if total == target:
                res.append(combo[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if total + candidates[i] > target:
                    break

                combo.append(candidates[i])
                dfs(i + 1, combo, total + candidates[i])
                combo.pop()

        dfs(0, [], 0)
        return res