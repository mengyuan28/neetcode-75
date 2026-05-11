class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m_len = len(nums)
        if m_len == 0:
            return True
        max_reach = 0
        for cur_pos in range(0, m_len):
            if cur_pos > max_reach:
                return False
            max_reach = max(max_reach, cur_pos + nums[cur_pos])
        return max_reach >= m_len-1