# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        total = 0
        def checkNodes(node: TreeNode, maxVal:int):
            nonlocal total
            if not node:
                return
            
            if node.val >= maxVal:
                total += 1
            
            currentMax = max(maxVal, node.val)
            checkNodes(node.left, currentMax)
            checkNodes(node.right, currentMax)
            

        checkNodes(root, root.val)
        return total

            


            