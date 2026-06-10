import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            res2 = nums.copy()
            res2.pop(i)
            x = math.prod(res2)
            res.append(x)
        return res

        