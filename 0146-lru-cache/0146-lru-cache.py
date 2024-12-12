class Node():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev, self.next = None, None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.hashmap = {} # key: address
        self.left, self.right = Node(None, None), Node(None, None)
        self.left.next, self.right.prev = self.right, self.left
    
    def addNode(self, node):
        # put in the rightmost
        prv = self.right.prev
        prv.next = self.right.prev = node
        node.prev, node.next = prv, self.right
    
    def deleteNode(self, node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # if the key exist, or not
        if key not in self.hashmap:
            return -1
        
        # update cache: delete -> add
        target = self.hashmap[key]
        self.deleteNode(target)
        self.addNode(target)
        return target.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.hashmap:
            target = self.hashmap[key]
            self.deleteNode(target)
        
        new = Node(key, value)
        self.hashmap[key] = new
        self.addNode(new)
        
        if len(self.hashmap) > self.capacity:
            # delete the least recently used key
            lru = self.left.next
            del self.hashmap[lru.key]
            self.deleteNode(lru)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)