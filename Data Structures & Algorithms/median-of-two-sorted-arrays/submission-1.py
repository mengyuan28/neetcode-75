class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        n1 = len(nums1)
        n2 = len(nums2)
        left_size = (n1+1+n2) //2
        lo, hi = 0, n1
        # 二分的是 A 左侧元素数量，可以是 0 到 n1
        # A[:i] | A[i:] vs B[:j] | B[j:]
        # ..A_left | A_right, vs B_left | B_right
        while lo <= hi:
            i = (lo + hi) //2 # size
            j = left_size -i
            a_left = nums1[i-1] if i > 0 else float("-inf")
            a_right = nums1[i] if i < n1 else float("inf")

            b_left = nums2[j-1] if j > 0 else float("-inf")
            b_right = nums2[j] if j < n2 else float("inf")

            if a_left > b_right:
                hi = i-1

            elif b_left > a_right:
                lo = i+1
            
            else:
                left_max = max(a_left, b_left)
                if (n1 + n2) %2 == 1:
                    return float(left_max)
                right_min = min(a_right, b_right)
                return (left_max + right_min) /2 

        
