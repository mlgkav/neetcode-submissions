# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

    def to_list(self):
        curr = self
        vals = []

        while curr:
            vals.append(curr.val)
            curr = curr.next     
        
        return vals
    
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # splice the first half and the reversed second half together

        # find the mid point
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        # reverse the second half
        curr = slow.next
        prev = 0

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        slow.next = None
        
        # prev now begins the reversed second half
        first, second = head, prev
        # print(first.to_list())
        # print(second.to_list())
        while second:
            first_next, second_next = first.next, second.next
            first.next, second.next = second, first_next
            first, second = first_next, second_next
        
