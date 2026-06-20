class Solution:
    def removeElement(self, nums: List[int], val: int) -> int: 
        l = 0
        while len(nums) > l:
            if nums[l] == val:
                del nums[l]
                continue
            else:
                l+=1

        k = len(nums)
        return k
            

                

        