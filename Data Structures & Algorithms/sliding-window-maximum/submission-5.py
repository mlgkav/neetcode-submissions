class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()

        # build the initial monotonically non-increasing deque
        for i in range(k):
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()
            dq.append(i)
        
        res = [nums[dq[0]]]
        for i in range(k, len(nums)):
            if dq[0] == i - k:
                dq.popleft()
            
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()
            dq.append(i)

            res.append(nums[dq[0]])
        
        return res