# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root.left is None and root.right is None:
            return 0
            
        longest = 0
        def findLongest(root: Optional[TreeNode]) -> int:
            nonlocal longest
            if not root:
                return 0
            if root.left is None and root.right is None:
                return 1
            left = findLongest(root.left)
            right = findLongest(root.right)
            cur_len = left + right + 1
            longest = max(cur_len, longest)
            return max(left, right) + 1

        findLongest(root)
        return longest-1
        