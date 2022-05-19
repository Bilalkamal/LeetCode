# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new = ListNode(-10000)
        dummy = new
        while head:
            if head.val > new.val:
                new.next = ListNode(head.val)
                new = new.next
            head = head.next
        
        return dummy.next