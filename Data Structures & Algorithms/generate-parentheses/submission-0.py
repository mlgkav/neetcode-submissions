class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(s, unclosed, remaining):
            if not unclosed and not remaining:
                res.append("".join(s))
                return

            if remaining:
                s.append("(")
                dfs(s, unclosed + 1, remaining - 1)
                s.pop()

            if unclosed:
                s.append(")")
                dfs(s, unclosed - 1, remaining)
                s.pop()

        dfs([], 0, n)
        return res