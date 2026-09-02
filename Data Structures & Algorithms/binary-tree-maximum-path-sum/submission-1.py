# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float("-inf")
        def dfs(root): # returns the maximum depth path from root
            if not root:
                return 0
            
            max_left, max_right = max(dfs(root.left), 0), max(dfs(root.right), 0)
            self.res = max(self.res, root.val + max_left + max_right)

            return root.val + max(max_left, max_right)
        dfs(root)
        return self.res

        