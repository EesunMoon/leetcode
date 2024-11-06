class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.cqueue = [-1] * k
        self.total = k
        self.start = 0
        self.count = 0

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.count != self.total:
            self.cqueue[(self.start + self.count) % self.total] = value
            self.count += 1
            return True
        return False
        

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.count != 0:
            self.cqueue[self.start] = -1
            self.start = (self.start+1)%self.total
            self.count -= 1
            return True
        return False
        

    def Front(self):
        """
        :rtype: int
        """
        return self.cqueue[self.start] if not self.isEmpty() else -1

    def Rear(self):
        """
        :rtype: int
        """
        return self.cqueue[(self.start + self.count -1)%self.total] if not self.isEmpty() else -1
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.count ==0
        

    def isFull(self):
        """
        :rtype: bool
        """
        return self.count == self.total


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()