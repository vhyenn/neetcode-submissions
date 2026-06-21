import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        heapq.heapify(nums)
        new_list = [0] * len(nums)

        for i in range(len(nums)):
            minn = heapq.heappop(nums)
            new_list[i] = minn
        return new_list

        