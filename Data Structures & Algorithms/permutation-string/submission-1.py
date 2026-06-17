class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1) - 1

        while len(s2) > r:
            strr = ""
            for i in range(l, r+1):
                strr += s2[i]
            
            if sorted(s1) == sorted(strr):
                return True
            
            l += 1
            r += 1
            continue
        return False


                
                

        
            
                
            





