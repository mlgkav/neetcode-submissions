class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(i, comb):
            if len(comb) == k:
                res.append(comb[:])
                return
            if i + (k - len(comb)) > n + 1: # short circuit if there are not enough numbers left to choose from
                return
            comb.append(i)
            dfs(i + 1, comb)
            comb.pop()
            dfs(i + 1, comb)
        dfs(1, [])
        return res
            
        