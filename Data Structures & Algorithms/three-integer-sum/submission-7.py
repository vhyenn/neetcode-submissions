class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        h = {}
        s = set()
        for i, num in enumerate(nums):
            h[num] = i

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                desired = -nums[i] - nums[j]
                if desired in h and h[desired] != i and h[desired] != j:
                    s.add(tuple(sorted([nums[i], nums[j], desired])))
        return list(s)
            



        


        
            

        