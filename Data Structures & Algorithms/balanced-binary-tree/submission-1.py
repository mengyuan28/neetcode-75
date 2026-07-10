class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def getHeight(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left_h = getHeight(node.left)
            if left_h == -1:
                return -1
            right_h = getHeight(node.right)
            if right_h == -1:
                return -1
            if abs(left_h - right_h) > 1:
                return -1
            return max(left_h, right_h) + 1

        return getHeight(root) != -1