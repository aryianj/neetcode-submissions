class MyHashMap:

    def __init__(self):
        self.hashMap = []

    def put(self, key: int, value: int) -> None:
        for l in self.hashMap:
            if key == l[0]:
                self.hashMap.remove(l)
        self.hashMap.append([key, value])

    def get(self, key: int) -> int:
        for l in self.hashMap:
            if key == l[0]:
                return l[1]
        return -1

    def remove(self, key: int) -> None:
        for l in self.hashMap:
            if key == l[0]:
                self.hashMap.remove(l)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)