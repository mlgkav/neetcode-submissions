"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        curr, copy = head, dummy

        """
        The key is to store the copied node in curr.random and curr.random in copy.random
        """

        # build list
        while curr:
            copy.next = Node(x=curr.val, random=curr.random)
            curr.random = copy.next
            curr, copy = curr.next, copy.next

        # fix the next and random pointers 
        curr, copy = head, dummy.next
        while curr:
            # update the next pointer using the copied node stored in curr.next.random
            copy.next = curr.next.random if curr.next else None

            # update the random pointer (didn't update the original list for simplicity)
            # original random is stored in copy.random
            copy.random = copy.random.random if copy.random else None
            curr, copy = curr.next, copy.next
        
        return dummy.next

