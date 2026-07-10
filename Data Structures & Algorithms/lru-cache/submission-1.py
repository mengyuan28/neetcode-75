class Node:
    def __init__(self, key: int, val:int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node(-1,-1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.checking: Dict[int, Node] = {}
        self.capacity = capacity

    def move_to_head(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        if prev_node and next_node:
            prev_node.next = next_node
            next_node.prev = prev_node
        new_next = self.head.next
        self.head.next = node
        node.next = new_next
        new_next.prev = node
        node.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.checking:
            return -1
        cur_node = self.checking.get(key)
        self.move_to_head(cur_node)
        return cur_node.val

    def remove_last_node(self):
        last_node = self.tail.prev
        if last_node != self.head:
            new_last_node = last_node.prev
            new_last_node.next = self.tail
            self.tail.prev = new_last_node

            del self.checking[last_node.key]

    def put(self, key: int, value: int) -> None:
        if key not in self.checking:
            cur_size = len(self.checking)
            if cur_size == self.capacity:
                self.remove_last_node()
            new_node = Node(key, value)
            self.move_to_head(new_node)
            self.checking[key] = new_node
        else:
            node = self.checking.get(key)
            node.val = value
            self.move_to_head(node)

            



            
        
