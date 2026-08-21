class Solution:
    # remember sums to 0
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        while i < len(nums) - 2:
            target = -nums[i]
            j, k = i + 1, len(nums) - 1
            while j < k:
                two_sum = nums[j] + nums[k]
                if two_sum > target:
                    k -= 1
                elif two_sum < target:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    # skip duplicates
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
            
            # skip duplicates
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        
        return res