class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, combo, combo_sum):
            if combo_sum == target:
                res.append(combo[:])
                return

            if (
                i == len(candidates)
                or combo_sum + candidates[i] > target
            ):
                return

            # Include this exact array element.
            combo.append(candidates[i])
            dfs(i + 1, combo, combo_sum + candidates[i])
            combo.pop()

            # Skip every remaining duplicate of this value.
            while (
                i + 1 < len(candidates)
                and candidates[i] == candidates[i + 1]
            ):
                i += 1

            dfs(i + 1, combo, combo_sum)

        dfs(0, [], 0)
        return res