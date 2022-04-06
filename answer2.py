from datetime import datetime
from collections import defaultdict
import math

class data():
    def __init__(self, key, value, weight):
        self.key = key
        self.value = value
        self.weight = weight
        self.accessedTime = datetime.now()
        self.score = 0

class scoreCache():
    def __init__(self, capacity):
        self.cache = defaultdict()
        self.capacity = capacity
        self.size = 0
        
    def put(self, key, value, weight):
        
        if key not in self.cache:
            new_data = data(key, value, weight)
            self.cache[new_data.key] = new_data
            self.size += 1
            if self.size == self.capacity:
                self.removeLowestScore()
                self.size -= 1
        else:
            update_data = data(key, value, weight)
            self.cache[key] = update_data
            
    def removeLowestScore(self):
        cur_time = datetime.now()
        
        for item in self.cache.items():
            if cur_time != item.accessedTime:
                item.score = item.weight /math.log(cur_time -item.accessedTime + 1 ) 
            else:
                item.score = item.weight/(-100)
        sorted_score = sorted(self.cache.items(), key = lambda data : data.score)
        
        least_score = sorted_score[0]
        del self.cache[least_score.key]
        
    def get(self, key):
        if key in self.cache:
            data = self.cache[key]
            data.accessedTime = datetime.now()
            return data.value
        else:
            return -1
# Time: get:O(1), put:O(N)
# Space: O(N)