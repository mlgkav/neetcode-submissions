from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        max_len = max(map(len, wordDict), default=0)

        @cache
        def dfs(start):
            if start == len(s):
                return True
            for end in range(start + 1, min(len(s), start + max_len) + 1):
                if s[start:end] in word_set and dfs(end):
                    return True
            
            return False
               

        return dfs(0)
