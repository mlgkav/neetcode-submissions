# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root, max):
            if not root:
                return 0
            if root.val >= max:
                return 1 + helper(root.left, root.val) + helper(root.right, root.val)
            return helper(root.left, max) + helper(root.right, max)
                

        return helper(root, float("-inf"))