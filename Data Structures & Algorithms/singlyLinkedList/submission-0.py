class ListNode:
    def __init__(self, val:int, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        cur = self.head.next
        i = 0
        while cur:
            if i == index:
                return cur.val
            i +=1
            cur = cur.next
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        cur = self.head
        i = 0
        while cur:
            if i == index:
                to_remove = cur.next                    
                if to_remove == self.tail:
                    self.tail = cur
                if not to_remove:
                    return False
                cur.next = to_remove.next
                return True
            i += 1
            cur = cur.next
        return False

    def getValues(self) -> List[int]:
        cur = self.head.next
        ret = []
        while cur:
            ret.append(cur.val)
            cur = cur.next
        return ret
