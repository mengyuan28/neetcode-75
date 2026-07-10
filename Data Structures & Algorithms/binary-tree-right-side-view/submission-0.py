# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ret = []
        track = deque()
        track.append(root)
        while track:
            cur_size = len(track)
            for i in range(0, cur_size):
                cur_front = track.popleft()
                if i == cur_size-1:
                    ret.append(cur_front.val)
                if cur_front.left:
                    track.append(cur_front.left)
                if cur_front.right:
                    track.append(cur_front.right)
        return ret
