class LinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LRU_Cache(object):

    def __init__(self, capacity = 5):
        # Initialize class variables
        self.buckets = [None for _ in range(capacity)]
        self.deque = []
        self.capacity = capacity
        self.current_size = 0
        pass


    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.

        hash_val = self.get_hash_code(key)

        if self.buckets[hash_val] is None:
            return -1

        head = self.buckets[hash_val]

        while head is not None:
            if head.key == key:
                self.mark_key_as_touched(key)
                return head.value
            head = head.next

        return -1
        pass

    #Whenever a key is used from the cache, move the resource to the top of the queue
    def mark_key_as_touched(self, key):
        print("mark as read for ::" + str(key))
        index = 0
        for num in self.deque:
            if num == key:
                break
            index += 1

        self.deque.pop(index)
        self.deque.append(key)
        print(self.deque)

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.

        hash_val = self.get_hash_code(key)

        #Remove the least recently used element from the queue.
        if self.current_size == 5:
            self.remove_least_used()

        #When there is a collision, perform chaining of the key value pair in the existing bucket.
        if self.buckets[hash_val] is not None:
            head = self.buckets[hash_val]
            while head.next is not None:
                head = head.next
            head.next = LinkedListNode(key, value)
        else: # when there is no collision
            self.buckets[hash_val] = LinkedListNode(key, value)

        self.deque.append(key)

        #Update the current size of the cache.
        self.current_size += 1
        pass

    def get_hash_code(self, key):
        return key % self.capacity

    def remove_least_used(self):
        least_used_key = self.deque.pop(0)
        hash_val = self.get_hash_code(least_used_key)
        head = self.buckets[hash_val]

        if head.key == least_used_key:
            self.buckets[hash_val] = head.next
            self.current_size -= 1
            return

        current = head.next
        previous = head

        while current:
            if current.key == least_used_key:
                previous.next = current.next
                self.current_size -= 1
                return
            current = current.next
        return
        pass


our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

print("getting value")
assert our_cache.get(1) == 1       # returns 1
assert our_cache.get(2) == 2      # returns 2
assert our_cache.get(9) == -1     # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

assert our_cache.get(3) == -1
