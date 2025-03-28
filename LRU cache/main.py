"""Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

1. LRUCache(int capacity) - Initialize the LRU cache with positive size capacity.
2. int get(int key) - Return the value of the key if the key exists, otherwise return -1.
3. void put(int key, int value) - Update the value of the key if the key exists.
Otherwise, add the key-value pair to the cache.
If the number of keys exceeds the capacity from this operation,
evict the least recently used key.
The functions get and put must each run in O(1) average time complexity."""
from collections import defaultdict, deque


# Time complexity: O(1) for both get and put
# Space complexity: O(capacity)
class LRUCache:
    def __init__(self, capacity: int):
        self.c = capacity
        self.m = defaultdict(int)
        self.deq = deque()

    def get(self, key: int) -> int:
        if key not in self.m:
            return -1
        val = self.m[key]
        # remove that key from deque and then append it back to deque
        # to make it to be the most recently used.
        if key != self.deq[len(self.deq) - 1]:
            self.deq.remove(key)
            self.deq.append(key)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            self.deq.remove(key)
        elif len(self.deq) == self.c:
            lru = self.deq.popleft()
            del self.m[lru]
        self.m[key] = value
        self.deq.append(key)


"""Double linked list version"""


class Node:
    def __init__(self, k: int, v: int):
        self.key = k
        self.val = v
        self.prev: Node | None = None
        self.next: Node | None = None


class LRUCache_db_linked_list:
    def __init__(self, capacity: int):
        self.c = capacity
        self.m: dict[int, Node] = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.m: return -1
        n = self.m[key]
        # check if node is already at most recently used (mru) position,
        # if satisfied, we don't need to remove and append
        if n != self.tail.prev:
            self._remove(n)
            self._append(n)
        return n.val

    def put(self, key: int, value: int) -> None:
        n = Node(k=key, v=value)
        if key in self.m:
            self._remove(self.m[key])
        # if the number of keys exceeds the capacity,
        # evict the least recently used node.
        elif len(self.m) == self.c:
            lru = self.head.next
            self._remove(lru)
            del self.m[lru.key]
        self.m[key] = n
        self._append(n)

    def _remove(self, node: Node) -> None:
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _append(self, node: Node) -> None:
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.next = self.tail
        node.prev = p


lru_cache = LRUCache_db_linked_list(2)
lru_cache.put(1, 1)
lru_cache.put(2, 2)
lru_cache.get(1)
lru_cache.put(3, 3)
lru_cache.get(2)
