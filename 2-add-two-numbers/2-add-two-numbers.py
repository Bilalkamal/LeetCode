# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = []
        while l1.next:
            n1.insert(0,l1.val)
            l1 = l1.next
        n1.insert(0,l1.val)
        
        n2 = []
        while l2.next:
            n2.insert(0,l2.val)
            l2 = l2.next
        n2.insert(0,l2.val)
        
        n1 = int("". join([str(n) for n in n1]))
        n2 = int("". join([str(n) for n in n2]))
        total = n1 + n2
        answer = [n for n in str(total)][::-1]
        
        cur = final = ListNode(0)
        for e in answer:
            cur.next = ListNode(e)
            cur = cur.next
        return final.next


        