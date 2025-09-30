class Node:
    def __init__(self, key, prev=None, next=None):
        self.key = key
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.left, self.right = Node(0), Node(0)
        self.left.next, self.right.prev = self.right, self.left
        self.map = {} # val: address
    
    def _length(self):
        return len(self.map)
    
    def pushRight(self, key): # for new Node
        node = Node(key, self.right.prev, self.right)
        self.map[key] = node
        node.prev.next, self.right.prev = node, node

    def pop(self, key): # remove target node
        if key in self.map:
            node = self.map[key]
            prevNode, nextNode = node.prev, node.next
            prevNode.next, nextNode.prev = nextNode, prevNode
            self.map.pop(key, None)

    def popLeft(self): # remove LRU
        target = self.left.next.key
        self.pop(target)
        return target
    
    def update(self, key): # if using the node
        self.pop(key)
        self.pushRight(key)
        
class LFUCache:

    def __init__(self, capacity: int):
        self.total = capacity
        self.lfuCnt = 0
        self.valMap = {} # key: val
        self.countMap = collections.defaultdict(int) # key: count
        self.listMap = collections.defaultdict(LinkedList) # count: LL

    def counter(self, key):
        cnt = self.countMap[key]
        self.countMap[key] += 1
        self.listMap[cnt].pop(key)
        self.listMap[cnt+1].pushRight(key)
        
        if cnt == self.lfuCnt and self.listMap[cnt]._length() == 0:
            self.lfuCnt += 1

    def get(self, key: int) -> int:
        if key not in self.valMap:
            return -1
        self.counter(key)
        return self.valMap[key]

    def put(self, key: int, value: int) -> None:
        if self.total == 0:
            return
        
        if key not in self.valMap and len(self.valMap) == self.total:
            lru = self.listMap[self.lfuCnt].popLeft()
            self.valMap.pop(lru)
            self.countMap.pop(lru)

        self.valMap[key] = value
        self.counter(key)
        self.lfuCnt = min(self.lfuCnt, self.countMap[key])


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)