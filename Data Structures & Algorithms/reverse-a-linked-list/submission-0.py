# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
       #if not head:
        #return []
        i=0
        prev=None
        curr=head
      
        while curr is not None:

        # store next
            nextNode = curr.next

        # reverse current node's next pointer
            curr.next = prev

        # move pointers one position ahead
            prev = curr
            curr = nextNode

        return prev

