# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        while curr:
            if curr.left: # left subtree exists
                # find the predecessor
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right

                if pred.right: # have already traversed predecessor so process current
                    k -= 1
                    if k == 0:
                        return curr.val
                    pred.right = None
                    curr = curr.right # current processed, move onto to next node
                else: # thread predecessor to current
                    pred.right = curr
                    curr = curr.left # process next node
            else: # no left subtree exists
                k -= 1
                if k == 0:
                    return curr.val
                curr = curr.right