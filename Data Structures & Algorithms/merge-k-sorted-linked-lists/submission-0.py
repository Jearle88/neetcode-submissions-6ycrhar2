# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        def mergeTwoLists( list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            if not list1 and not list2:
                return None
            if not list1 and list2:
                return list2
            if not list2 and list1:
                return list1
        
            curr1=list1
            curr2=list2
            r_l=[]
            r=None
            if curr1.val<=curr2.val:
                r_l.append(curr1.val)
                r=curr1
                curr1=curr1.next   
           
            else:
                r_l.append(curr2.val)
                r=curr2
                curr2=curr2.next
            dummy=r
            while curr1 and curr2:
                if curr1.val<= curr2.val:
                    r_l.append(curr1.val)
                    r.next=curr1
                    r=r.next
                    curr1=curr1.next
                #r_l.append(curr1.val)
                else:
                    r_l.append(curr2.val)
                    r.next=curr2
                    r=r.next
                    curr2=curr2.next
                
            if curr1:
                while curr1:
                    r_l.append(curr1.val)
                    r.next=curr1
                    r=r.next
                    curr1=curr1.next

            if curr2:
                while curr2:
                    r_l.append(curr2.val)
                    r.next=curr2
                    r=r.next
                    curr2=curr2.next
        #print("ORer",r_l)
            return dummy
 
        final_v=lists[0]
        for i in range(1,len(lists)):
            final_v=mergeTwoLists(final_v,lists[i])
        return final_v
