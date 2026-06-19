class Solution:

    def replaceElements(self, arr: List[int]) -> List[int]:
        
        myarr = []
        for i in range(len(arr) - 1):
            x = []
            for j in range(i + 1, len(arr)):
                x.append(arr[j])
            
            myarr.append(max(x))
        
        myarr.append(-1)
        
        return myarr

                
            








            
        