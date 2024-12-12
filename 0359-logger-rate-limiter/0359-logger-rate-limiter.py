class Logger(object):

    def __init__(self):
        self.hashmap = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        time = self.hashmap.get(message, 0)
        if time > timestamp:
            return False
        
        self.hashmap[message] = timestamp + 10
        return True
        
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)