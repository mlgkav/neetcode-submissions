class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            # if m is in left sorted portion
            if nums[m] >= nums[l]:
                # if target is in left half
                if target >= nums[l] and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # if m is in right sorted portion
            else:
                # if target is in right side
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1