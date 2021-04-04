# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        queue = []
        queue.append(root)
        
        
        result = []
        if root is None:
            return  result
        
        
        
        while queue:
            inter = []
            for i in range(len(queue)):
                current_node = queue.pop(0)
                inter.append(current_node.val)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            result.append(inter)
        
        return result
