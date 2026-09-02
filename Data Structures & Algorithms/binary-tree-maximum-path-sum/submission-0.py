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
            
            max_left, max_right = dfs(root.left), dfs(root.right)
            self.res = max(
                self.res,
                max_left + root.val,
                max_right + root.val,
                max_left + max_right + root.val,
                root.val
            )

            return max(
                max_left + root.val,
                max_right + root.val,
                root.val
            )
        dfs(root)
        return self.res

        