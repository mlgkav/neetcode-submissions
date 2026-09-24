from functools import cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def helper(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            res = helper(i + 1, j + 1)
            if text1[i] == text2[j]:
                res += 1

            res = max(res, helper(i + 1, j), helper(i, j + 1))
            return res

        return helper(0, 0)