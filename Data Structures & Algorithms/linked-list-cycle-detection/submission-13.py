# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=head
        i=0
        if not head:
            return False
        if not slow.next or not  slow.next.next:
            return False
        fast=slow.next.next
       
        while slow.next and (fast and fast.next and  fast.next.next):
            if fast.val==slow.val:
                return True
            else:
                slow=slow.next
                fast=fast.next.next
        return False
            
