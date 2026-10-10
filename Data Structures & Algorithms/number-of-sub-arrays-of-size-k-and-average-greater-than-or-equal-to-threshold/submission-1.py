class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curr_avg = sum(arr[:k]) / k
        res = int(curr_avg >= threshold)
        for r in range(k, len(arr)):
            curr_avg += arr[r] / k
            curr_avg -= arr[r - k] / k
            res += int(curr_avg >= threshold)
        return res
