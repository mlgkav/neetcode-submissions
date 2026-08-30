# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)

        tail, prev_group_tail = head, dummy
        group_count = 0
        while tail:
            tail = tail.next
            group_count += 1

            if group_count == k:
                curr = prev_group_tail.next # first node in current group
                prev = tail # first node in next group
                while curr != tail:
                    next = curr.next
                    curr.next = prev
                    prev = curr
                    curr = next

                # prev = head of reversed list
                curr_group_tail = prev_group_tail.next
                prev_group_tail.next = prev # stich reversed list to previous group's tail
                prev_group_tail = curr_group_tail

                group_count = 0

        return dummy.next