class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.left, self.right = Node(-1,-1), Node(-1,-1)
        self.left.next, self.right.prev = self.right, self.left
        self.Map = {} # key: address

    def pushRight(self, node):
        prevN, nextN = self.right.prev, self.right
        node.prev, node.next = prevN, nextN
        prevN.next, nextN.prev = node, node

    def pop(self, node):
        prevN, nextN = node.prev, node.next
        prevN.next, nextN.prev = nextN, prevN
        return node

    def touch(self, key):
        node = self.pop(self.Map[key])
        self.pushRight(node)

    def get(self, key: int) -> int:
        if key not in self.Map:
            return -1
        self.touch(key)
        return self.Map[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.Map:
            self.Map[key].val = value
            self.touch(key)
            return

        if len(self.Map) == self.cap:
            LRU = self.left.next
            self.Map.pop(LRU.key)
            self.pop(LRU)
            

        newNode = Node(key, value)
        self.pushRight(newNode)
        self.Map[key] = newNode
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)