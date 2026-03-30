# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        prev=None
        curr1=head
        curr2=head.next
        lz=head
        l=0
        curr_l=0
        while lz:
            l+=1
            lz=lz.next

        #print("length",l)
        if l==1:
            return None
        if l==2:
            if n==1:
                head.next=None
                return head
            else:
                head=head.next
                return head
        
        pos=l-n
        print("pos",pos)
        while curr1 and curr_l<=l:
            if curr_l==pos:
                if prev==None:
                    head=head.next
                    return head
                else:
                    prev.next=curr1.next
                    break
            curr_l+=1
            prev=curr1
            curr1=curr1.next
        return head

        
        

        