class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = len(s1)
        r = len(s2)
        if l > r:
            return False
        x = [0] * 26
        y = [0] * 26



        for i in range(len(s1)):
            charr = ord(s1[i]) - ord('a')
            x[charr] += 1
            charr2 =  ord(s2[i]) - ord('a')
            y[charr2] += 1
        if x == y:
            return True
        
        for i in range(l, r):
            count1 = ord(s2[i]) - ord("a")
            y[count1] += 1
            count2 = ord(s2[i - l]) - ord("a")
            y[count2] -= 1
            if x == y:
                return True

        return False
        
        


        
            

        


                
                

        
            
                
            





