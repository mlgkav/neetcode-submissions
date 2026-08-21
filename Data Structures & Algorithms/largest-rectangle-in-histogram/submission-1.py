class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (height, left index)
        res = 0

        for r, h_r in enumerate(heights):
            l = -1 # stores left index for rectangle with current bar_height
        
            # iterate through all rectangle with heights greater than current bar
            while stack and stack[-1][0] >= h_r:
                h_l, l = stack.pop()
                res = max(res, h_l*(r - l))
            
            # update stack with current height bar rectangle and its left index
            if l != -1:
                stack.append((h_r, l))
            else:
                stack.append((h_r, r))
       
        # compute areas of remaining rectangles
        while stack:
            h_l, l = stack.pop()
            res = max(res, h_l*(len(heights) - l))
        
        return res


