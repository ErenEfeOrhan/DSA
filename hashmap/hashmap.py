class Node:
    def __init__(self, key, data):
        self.key= key
        self.value = data
        self.next = None

class HashMap:
    def __init__(self, inital_capacity=8):
        self.capacity = inital_capacity
        self.size = 0
        self.buckets = [None] * self.capacity
    
    def _get_hash(self, key):
        return hash(key) % self.capacity
    
    def _get_load_factor(self):
        return self.size / self.capacity
    
    def put(self, key, value):
        index = self._get_hash(key)
        if self.buckets[index] == None:
            self.buckets[index] = Node(key,value)
            self.size +=1
        else:
            head = self.buckets[index]
            while head is not None:
                if head.key == key:
                    head.value = value
                    return
                if head.next is None:
                    break
                head = head.next
            head.next = Node(key,value)
            self.size +=1
        if self._get_load_factor() > 0.7:
            self.resize()

    def resize(self):
        print(f"--> Load factor exceeded 0.7! Resizing from {self.capacity} to {self.capacity * 2}...")
        old_buckets = self.buckets
        self.capacity *=2
        self.size = 0
        self.buckets = [None] * self.capacity
        
        for head in old_buckets:
            current = head
            while current is not None:
                self.put(current.key, current.value)
                current = current.next

    def get(self, key):
        index = self._get_hash(key)
        head = self.buckets[index]
        if head is None:
            return None

        while head is not None:
            if head.key == key:
                return head.value , index
            head = head.next
    
    def remove(self, key):
        index = self._get_hash(key)
        head = self.buckets[index]
        if head is None:
            return None
        current = head
        prev = None
        while current is not None:
            if head.key == key:
                self.buckets[index] = head.next
                self.size -=1
                return True
            prev = current
            current = current.next
            if current.key == key:
                prev.next = current.next
                self.size -= 1
                return True
            
my_map = HashMap(inital_capacity=4)
my_map.put("apple", 5)
my_map.put("avocado", 7)
my_map.put("watermelon", 10)
my_map.put("kiwi", 4)
my_map.put("orange", 3)
my_map.put("strawberry", 15)


print(f"apple price is",my_map.get("apple"))
print(f"avocado price is",my_map.get("avocado"))
print(f"watermelon price is",my_map.get("watermelon"))
print(f"kiwi price is",my_map.get("kiwi"))
print(f"orange price is",my_map.get("orange"))
print(f"strawberry price is",my_map.get("strawberry"))

my_map.remove("watermelon")
print(f"watermelon price is",my_map.get("watermelon"))

print("Current capacity is now:", my_map.capacity)




        

        