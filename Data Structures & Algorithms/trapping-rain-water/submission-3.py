class Solution:
    def trap(self, height: List[int]) -> int:
        # this is a prefix postfix to store the largest amount of 
        water = [0] * len(height)
        pre = 0
        for i, h in enumerate(height):
            pre = max(pre, h)
            water[i] = pre - h
        
        post = 0
        for i in range(len(height) - 1, -1 , -1):
            post = max(post, height[i])
            water[i] = min(water[i], post - height[i])
        
        return sum(water)
