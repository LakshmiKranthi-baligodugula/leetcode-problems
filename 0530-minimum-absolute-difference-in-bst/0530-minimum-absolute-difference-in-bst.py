# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getMinimumDifference(self, node: Optional[TreeNode]) -> int:
        self.prev = None
        self.min_dif = float("inf")
        
        def inorder(node):
            if node is None:
                return
            
            inorder(node.left)
            
            if self.prev is not None:
                cur_dif = node.val - self.prev
                self.min_dif = min(self.min_dif, cur_dif)
            
            self.prev = node.val
            
            inorder(node.right)
            
        inorder(node)
        return self.min_dif
