class Solution:

    def replaceElements(self, arr: List[int]) -> List[int]:
        
        myarr = []
        l = 0
        while l < len(arr) - 1:
            x = 0
            for r in range(l+1, len(arr)):
                x = max(x, arr[r])
            myarr.append(x)
            l+=1 
        myarr.append(-1)
        return myarr
            
                



                
            








            
        