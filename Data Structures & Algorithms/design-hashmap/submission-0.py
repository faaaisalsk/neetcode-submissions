class MyHashMap:

    def __init__(self):
        self.hashmap = []

    def put(self, key: int, value: int) -> None:
        for item in self.hashmap:
            if key == item[0]:
                item[1] = value
                return 
        self.hashmap.append([key, value])
        #return self.hashmap

    def get(self, key: int) -> int:
        for k,v in self.hashmap:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        for item in self.hashmap:
            if key == item[0]:
                self.hashmap.remove(item)
        #return self.hashmap


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)