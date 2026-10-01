class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1

            if len(counts) > 2:
                new_counts = defaultdict(int)
                for num, count in counts.items():
                    if count > 1:
                        new_counts[num] = count - 1 
                counts = new_counts
        
        return [num for num in counts if nums.count(num) > len(nums) // 3]