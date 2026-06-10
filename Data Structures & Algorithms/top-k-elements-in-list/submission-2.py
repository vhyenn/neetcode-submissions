from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}
        n = len(nums)
        buckets = [0] * (n+1)

        for i in nums:
            if i in myDict:
                myDict[i] += 1
            
            else:
                myDict[i] = 1
        
        for key, value in myDict.items():
            if buckets[value] == 0:
                buckets[value] = [key]
            else:
                buckets[value].append(key)
        maxNums = []
        for i in range(len(nums), -1, -1):
            if buckets[i] != 0:
                maxNums.extend(buckets[i])
            if len(maxNums) == k:
                break
        return maxNums
        
        
            
            

            
        
        



                
        
            
             


        
        