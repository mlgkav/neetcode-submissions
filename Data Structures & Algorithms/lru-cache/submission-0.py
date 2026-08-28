class Node:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key  # Required so we know which key to delete from hash map upon eviction
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_map = {}  # key -> Node

        # Sentinel nodes (head = LRU side, tail = MRU side)
        self.head = Node()
        self.tail = Node(prev= self.head)
        self.head.next = self.tail

    def _remove(self, node: Node) -> None:
        """Removes an existing node from the doubly linked list."""
        node.prev.next, node.next.prev = node.next, node.prev
        
    def _insert_at_tail(self, node: Node) -> None:
        """Inserts a node right before the tail sentinel (MRU position)."""
        tail_prev = self.tail.prev
        tail_prev.next, node.prev = node, tail_prev
        node.next, self.tail.prev = self.tail, node

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1

        node = self.node_map[key]
        # Move to MRU position
        self._remove(node)
        self._insert_at_tail(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            # Key exists: remove old node from list
            self._remove(self.node_map[key])
        elif len(self.node_map) == self.capacity:
            # Cache is full: evict LRU (node after head sentinel)
            lru_node = self.head.next
            self._remove(lru_node)
            del self.node_map[lru_node.key]

        # Add new node to MRU position
        new_node = Node(key, value)
        self._insert_at_tail(new_node)
        self.node_map[key] = new_node