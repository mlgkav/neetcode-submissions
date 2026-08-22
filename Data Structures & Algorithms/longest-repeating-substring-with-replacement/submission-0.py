class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        res = 0

        l = -1
        max_freq = 0
        for r, c in enumerate(s):
            count[c] += 1
            max_freq = max(max_freq, count[c])
            # key insight is that you don't have to update max_freq inside the while loop because it maintains the maximum until another maximum is found.
            while r - l - max_freq > k:
                l += 1
                count[s[l]] -= 1
            res = max(res, r - l)
        return res