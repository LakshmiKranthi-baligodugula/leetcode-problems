# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n==0:
            return []
        res={}
        def generate_trees(start,  end):
            if (start, end) in res:
                return res[(start, end)]
            trees=[]
            if start>end:
                trees.append(None)
                return trees
            for root_value in range(start, end+1):
                left_trees=generate_trees(start,root_value-1)
                right_trees=generate_trees(root_value+1,end)
                for left_tree in left_trees:
                    for right_tree in right_trees:
                        root = TreeNode(root_value, left_tree, right_tree)
                        trees.append(root)
            
            res[(start, end)] = trees
            return trees

        return generate_trees(1, n)
                