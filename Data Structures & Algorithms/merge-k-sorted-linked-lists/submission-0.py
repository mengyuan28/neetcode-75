# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node: ListNode):
        self.node = node
    
    def __lt__(self, other: ListNode):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        dummy = ListNode(-1)
        cur = dummy
        minHeap = []
        for node in lists:
            if node:
                heapq.heappush(minHeap, NodeWrapper(node))
        
        while minHeap:
            nodeWrapper = heapq.heappop(minHeap)
            cur.next = nodeWrapper.node
            cur = cur.next

            if nodeWrapper.node.next:
                heapq.heappush(minHeap, NodeWrapper(nodeWrapper.node.next))
        return dummy.next

