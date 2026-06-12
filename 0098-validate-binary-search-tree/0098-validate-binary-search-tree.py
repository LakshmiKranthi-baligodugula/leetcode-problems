# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(root,minimum,maximum):
            if root is None:
                return True
            if root.val<=minimum or root.val>=maximum:
                return False
            left=check(root.left,minimum,root.val)
            right=check(root.right,root.val,maximum)
            return left and right
        return check(root,float("-inf"),float("inf"))

