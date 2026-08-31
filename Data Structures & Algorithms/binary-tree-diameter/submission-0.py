# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def helper(root):
            if not root:
                return 0

            max_left, max_right = helper(root.left), helper(root.right)
            self.res = max(self.res, max_left + max_right)

            return 1 + max(max_left, max_right)

        helper(root)
        return self.res

        