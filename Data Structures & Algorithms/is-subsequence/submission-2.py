class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        l = 0
        r = 0
        strr = ""
        while len(t) > r and len(s) > l:
            if s[l] != t[r]:
                r += 1
                continue
            elif s[l] == t[r]:
                strr += t[r]
                l+=1
                r+=1
                continue
        if strr == s:
                return True
        return False

            
        

        

                
        