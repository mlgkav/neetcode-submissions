# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.pre_index = self.in_index = 0
        def dfs(limit):
            if self.pre_index >= len(preorder): # no more preorder nodes to process
                return None     
            if inorder[self.in_index] == limit: # reached inorder node
                self.in_index += 1
                return None

            root = TreeNode(preorder[self.pre_index])
            self.pre_index += 1
            root.left = dfs(root.val)
            root.right = dfs(limit)
            return root
        return dfs(float("inf"))
        