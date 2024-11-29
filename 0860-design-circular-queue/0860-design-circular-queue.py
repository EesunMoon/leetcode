class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.size = k
        self.queue = [-1] * self.size
        self.start, self.cnt = 0, 0

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if not self.isFull():
            self.queue[(self.start + self.cnt)%self.size] = value
            self.cnt += 1
            return True
        return False

    def deQueue(self):
        """
        :rtype: bool
        """
        if not self.isEmpty():
            self.start = (self.start + 1) % self.size
            self.cnt -= 1
            return True
        return False

    def Front(self):
        """
        :rtype: int
        """
        return self.queue[self.start] if not self.isEmpty() else -1

    def Rear(self):
        """
        :rtype: int
        """
        return self.queue[(self.start+self.cnt-1)%self.size] if not self.isEmpty() else -1

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.cnt == 0
        

    def isFull(self):
        """
        :rtype: bool
        """
        return self.cnt == self.size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()