class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0

        for n in nums:
            if n - 1 not in s: # start of a sequence
                m = n + 1
                while m in s:
                    m += 1
                res = max(res, m - n)
        
        return res;