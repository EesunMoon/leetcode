class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {} # key: address
        self.head, self.tail = Node(0, 0), Node(0,0)
        self.head.next, self.tail.prev = self.tail, self.head

    def add(self, newNode):
        LLU = self.tail.prev
        LLU.next = self.tail.prev = newNode
        newNode.prev, newNode.next = LLU, self.tail

    def delete(self, node):
        prevNode, nextNode = node.prev, node.next
        prevNode.next, nextNode.prev = nextNode, prevNode
        
    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.delete(self.hashmap[key])
            self.add(self.hashmap[key])
            return self.hashmap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.delete(self.hashmap[key])

        newNode = Node(key, value)
        self.hashmap[key] = newNode
        self.add(newNode)
        
        if len(self.hashmap) > self.capacity: # delete LRU
            LRU = self.head.next
            self.delete(LRU)
            del self.hashmap[LRU.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)