class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        l = 0
        r = len(nums) - 1

        while l < r:
            if nums[l] + nums[r]  != target:
                if l + 1 != r:
                    l += 1
                else:
                    l = 0
                    r = r - 1
            else:
                return [l, r]
            

    
    
        