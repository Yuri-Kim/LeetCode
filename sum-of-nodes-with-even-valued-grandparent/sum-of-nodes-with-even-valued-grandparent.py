# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.answer = 0

        def dfs(root, parent, grandparent):
            if not root:
                return
            if grandparent and grandparent % 2 == 0:
                self.answer += root.val
            dfs(root.left, root.val, parent)
            dfs(root.right, root.val, parent)

        dfs(root, 0, 0)
        return self.answer
        
    
        
        