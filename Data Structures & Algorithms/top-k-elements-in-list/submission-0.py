from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = {}
        maxList = []

        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        for i in range(k):
            a = max(hashmap, key = hashmap.get)
            maxList.append(a)
            hashmap.pop(a)

        return maxList
            
             


        
        