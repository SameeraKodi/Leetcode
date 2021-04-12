# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        #want to do BFS on the root node
        if root is None:
            return result
        
        queue = []
        
        queue.append(root)
        
        while queue:
            sub = []
            l = len(queue)
            for i in range(l):
                current = queue.pop(0)
                sub.append(current.val)
                if current.left != None:
                    queue.append(current.left)
                if current.right != None:
                    queue.append(current.right)
                    
            result.append(sub)
        
        return result
        
        
#         if root is None:
#             return result
        
#         queue = []
#         queue.append(root)
        
#         result = []
    
#         while queue:
#             sub = []
#             l = len(queue)
#             for i in range(l):
#                 current = queue.pop(0)
#                 sub.append(current.val)
#                 if current.left != None:
#                     queue.append(current.left)
#                 if current.right != None:
#                     queue.append(current.right)
                    
#             result.append(sub)
#         return result

