class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = -1
        res = 0
        for r, c in enumerate(s):
            while c in char_set:
                l += 1
                char_set.remove(s[l])
            char_set.add(c)
            res = max(res, r - l)

        return res