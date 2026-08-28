class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # use Floyd's cycle detection algorithm
        slow = fast = 0
        while True: # cycle is guaranteed
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
