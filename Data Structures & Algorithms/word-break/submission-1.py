class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)

        memo = {}
        def dfs(start, end):
            if (start, end) not in memo:
                if start == len(s):
                    memo[(start, end)] = True
                elif end > len(s):
                    memo[(start, end)] = False
                elif s[start:end] in word_set and dfs(end, end):
                    memo[(start, end)] = True
                else:
                    memo[(start, end)] = dfs(start, end + 1)
            return memo[(start, end)]
            
        return dfs(0, 0)
