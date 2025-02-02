class RandomizedSet:

    def __init__(self):
        self.hashmap = {} # val: index
        self.list = []

    def insert(self, val: int) -> bool:
        # not present => insert & True, otherwise => False
        if val not in self.hashmap:
            self.hashmap[val] = len(self.list)
            self.list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False
        # swap with last element
        target_index = self.hashmap[val]
        last_element = self.list[-1]
        self.list[target_index] = last_element
        self.hashmap[last_element] = target_index

        # delete last element
        del self.hashmap[val]
        self.list.pop()
        return True

    def getRandom(self) -> int:
        return choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()