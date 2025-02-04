class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        # hashmap val:node address
        self.hashmap = {}
        self.head, self.tail = Node(-1, -1), Node(-1, -1)
        self.head.next, self.tail.prev = self.tail, self.head
        self.capacity = capacity
    
    def delete(self, node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv

    def add(self, node):
        prv = self.tail.prev
        prv.next, self.tail.prev = node, node
        node.prev, node.next = prv, self.tail

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        # get node -> move last index (delete, add)
        node = self.hashmap[key]
        self.delete(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        # existed: delete -> add (the last position)
        # not existed: add -> check exceed capacity
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value # update
            self.delete(node)
            self.add(node)
        else:
            node = Node(key, value)
            self.hashmap[key] = node
            self.add(node)
            if len(self.hashmap) > self.capacity:
                LRU = self.head.next
                del self.hashmap[LRU.key]
                self.delete(LRU)


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)