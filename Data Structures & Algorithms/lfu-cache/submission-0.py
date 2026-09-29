from collections import defaultdict, OrderedDict
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_freq = {}
        # Use OrderedDict for LRU cache impelmentation for O(1)
        self.freq_to_lru_cache = defaultdict(OrderedDict) # self.freq_to_lru_cache[freq][key] = (key, value)
        self.min_freq = 0
        

    def get(self, key: int) -> int:
        if key not in self.key_to_freq:
            return -1
        self._increment_freq(key)
        freq = self.key_to_freq[key]
        return self.freq_to_lru_cache[freq][key][1]
        

    def put(self, key: int, value: int) -> None:
        if key not in self.key_to_freq:
            if self.capacity == 0:
                self._evict()
                self.capacity += 1

            self.capacity -= 1
            self.key_to_freq[key] = self.min_freq = 1
            self.freq_to_lru_cache[1][key] = (key, value)
        else:
            freq = self.key_to_freq[key]
            self.freq_to_lru_cache[freq][key] = (key, value)
            self._increment_freq(key)


    def _increment_freq(self, key: int) -> None:
        assert key in self.key_to_freq # Sanity check

        freq = self.key_to_freq[key]
        lru_cache = self.freq_to_lru_cache[freq]
        _, value = lru_cache[key]

        # Remove existing entry in LRU cache
        del lru_cache[key]

        # Check whether LRU cache for old frequency is empty
        if not lru_cache:
            # Update mininum frequency if old frequency was minimum
            if self.min_freq == freq:
                self.min_freq += 1
            del self.freq_to_lru_cache[freq]

        # Promote key to next LRU cache
        freq += 1
        self.key_to_freq[key] = freq
        self.freq_to_lru_cache[freq][key] = (key, value)

    def _evict(self) -> None:
        lru_cache = self.freq_to_lru_cache[self.min_freq]
        key, _ = lru_cache.popitem(last=False)

        # Remove key
        del self.key_to_freq[key]

        # Check whether LRU cache for oldd frequency is empty
        if not lru_cache:
            del self.freq_to_lru_cache[self.min_freq]
            # No need to update min_freq because new key insertion happens immediately after


        
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)