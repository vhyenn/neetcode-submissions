class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1) - 1
        x = [0] * 26

        for i in range(len(s1)):
            charr = ord(s1[i]) - ord('a')
            x[charr] += 1
        
        while len(s2) > r:
            y = [0] * 26
            for i in range(l, r + 1):
                charr2 = ord(s2[i]) - ord('a')
                y[charr2] += 1

            if x == y:
                return True
            
            l += 1
            r += 1
            
        return False



        
            

        


                
                

        
            
                
            





