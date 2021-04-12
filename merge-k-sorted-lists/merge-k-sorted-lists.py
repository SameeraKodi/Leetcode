# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        current = head
        
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2= l2.next
                
            current = current.next
            
        #Cases when 1 listnode runs out
        
        if l1 != None:
            current.next = l1
            l1 = l1.next
        if l2 != None:
            current.next = l2
            l2 = l2.next
    
        return head.next
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        
        mid = len(lists)//2
        
        l1 = self.mergeKLists(lists[:mid])
        l2 = self.mergeKLists(lists[mid:])
        
        return self.mergeTwoLists(l1,l2)

            
        
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         #divide & conquer method
#         if len(lists) == 0:
#             return None
#         if len(lists) == 1:
#             return lists[0]
        
#         mid = len(lists)//2
        
#         l1 = self.mergeKLists(lists[:mid])
#         l2 = self.mergeKLists(lists[mid:])
#         return self.mergeTwoLists(l1,l2)
        
            


        

        
                
                
        