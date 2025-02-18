class RandomizedSet:

    def __init__(self):
        self.rand_set = []
        self.index = {}

    def insert(self, val: int) -> bool:
        if not val in self.index:
            n = len(self.rand_set)
            self.index[val] = n
            self.rand_set.append(val)
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        if val not in self.index:
            return False
        
        last_element = self.rand_set[-1]
        idx_remove = self.index[val]

        self.rand_set[idx_remove] = last_element

        self.index[last_element] = idx_remove

        self.rand_set.pop()
        self.index.pop(val)
        return True

            

    def getRandom(self) -> int:
        return random.choice(self.rand_set)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()