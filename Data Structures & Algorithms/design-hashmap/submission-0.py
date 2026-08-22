class MyHashMap:

    def __init__(self):
        self.size=5
        self.buckets=[[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        for pair in self.buckets[index]:
            if key == pair[0]:
                pair[1]=value
                return

        self.buckets[index].append([key,value])

    def get(self, key: int) -> int:
        index = key % self.size
        for pair in self.buckets[index]:
            if key == pair[0]:
                return pair[1]
            
        return -1
        

    def remove(self, key: int) -> None:
        index = key % self.size
        for pair in self.buckets[index]:
            if key == pair[0]:
                self.buckets[index].remove(pair)
        
        return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)