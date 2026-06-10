from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = {}
        hip = []

        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
            
        
        for key, value in hashmap.items():
            if len(hip) < k:
                heapq.heappush(hip, (value, key))
            else:
                heapq.heappushpop(hip, (value, key))
        
        return [i[1] for i in hip]
                
        
            
             


        
        