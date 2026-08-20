class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums) # O(n) time + space
        freqs = [[] for _ in range(len(nums))] # O(n) space

        for n, count in counts.items():
            freqs[count-1].append(n)
        
        res = []
        for freq in range(len(freqs) - 1, -1, -1):
            for n in freqs[freq]:
                res.append(n)
                if len(res) == k:
                    return res
        
        return res

"""
O(n) time - counting, adding to freqs, and enumerating freqs
O(n) space - counter, freqs, and result
"""