class Hash_table:
    
    def __init__(self, size=1000):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hashFunction(self, key):
        return sum([ord(c) for c in key]) % self.size
    
    def insert(self, key, value):
        index = self.hashFunction(key)
        self.table[index].append((key, value))
    
    def search(self, key):
        index = self.hashFunction(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None
    
    def delete(self, key):
        index = self.hashFunction(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False
    
    def __str__(self):
        return str(self.table)
                
