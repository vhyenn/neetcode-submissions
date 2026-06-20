class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        my_dict = {}
        for i in range(len(nums)):
            if nums[i] in my_dict.keys():
                my_dict[nums[i]] += 1
            else:
                my_dict[nums[i]] = 1
        
        res = max(my_dict, key=my_dict.get)
        
        return res
        