class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums) # O(n) time + space
        buckets = [[] for _ in range(len(nums))] # O(n) space

        for n, count in counts.items():
            buckets[count-1].append(n)
        
        res = []
        for count in range(len(buckets) - 1, -1, -1):
            for n in buckets[count]:
                res.append(n)
                if len(res) == k:
                    return res
        
        return res

"""
O(n) time - counting, adding to buckets, and enumerating buckets
O(n) space - counter, buckets, and result
"""