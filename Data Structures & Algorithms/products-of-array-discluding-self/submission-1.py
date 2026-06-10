import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        product = 1
        zero_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1

            else:
                product *= int(nums[i]) 

        
        if zero_count == 0:
            for i in range(len(nums)):
                res.append(int(product/int(nums[i])))
        elif zero_count == 1:
            for i in range(len(nums)):
                if nums[i] != 0:
                    res.append(0)
                else:
                    res.append(product)
        else:
            for i in range(len(nums)):
                res.append(0)
        return res
                
                

                
                
            
            



        