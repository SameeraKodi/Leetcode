# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        current = head
        
        while l1 != None and l2!= None:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
                
            else:
                current.next = l2
                l2 = l2.next
            
            current = current.next
            
        if l1 != None:
            current.next = l1
            l1 = l1.next
        if l2 != None:
            current.next = l2
            l2 = l2.next
            
        return head.next
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         head = ListNode(0)
#         current = head
        
#         while l1!= None and l2 !=None:
#             if l1.val < l2.val:
#                 current.next = l1
#                 l1 = l1.next
                
#             else:
#                 current.next = l2
#                 l2 = l2.next
            
#             current = current.next 
            
#         if l1 != None:
#             current.next = l1
#             l1 = l1.next
        
#         if l2 != None:
#             current.next = l2
#             l2 = l2.next
            
#         return head.next
            


        
        

        

        
        