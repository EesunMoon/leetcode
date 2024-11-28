class Logger(object):

    def __init__(self):
        self.time = 10
        self.store = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        x = self.store.get(message, 0)
        if x <= timestamp:
            self.store[message] = (self.time + timestamp)
            return True
        else:
            return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)