class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        res, res_len = "", float("inf")

        l = 0
        remaining_count = len(t)
        for r, c in enumerate(s):
            if c in count:
                if count[c] > 0:
                    remaining_count -= 1
                count[c] -= 1
            if remaining_count == 0:
                while s[l] not in count or count[s[l]] < 0:
                    if s[l] in count:
                        count[s[l]] += 1
                    l += 1
                sub_len = r - l + 1 
                if sub_len < res_len:
                    res, res_len = s[l:r + 1], sub_len

        return res
