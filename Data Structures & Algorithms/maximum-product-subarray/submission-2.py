class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        need to store the maximum and minimum products to account for the negative cases
        """
        max_prod = min_prod = res = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            new_max_prod = max(n * max_prod, n * min_prod, n)
            res = max(res, new_max_prod)
            new_min_prod = min(n * max_prod, n * min_prod, n)
            max_prod, min_prod = new_max_prod, new_min_prod

        return res