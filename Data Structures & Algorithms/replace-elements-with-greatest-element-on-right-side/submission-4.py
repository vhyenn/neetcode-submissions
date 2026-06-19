class Solution:

    def replaceElements(self, arr: List[int]) -> List[int]:
        maxx = -1
        new_arr = []
        for i in reversed(arr):
            new_arr.insert(0, maxx)
            maxx = max(i, maxx)
        
        return new_arr
            
        

            
            
                



                
            








            
        