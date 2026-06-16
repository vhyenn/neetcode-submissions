class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        maxx  = 0
        sett = set()

        for r in range(len(s)):
            while s[r] in sett:
                
                sett.remove(s[l])
                l += 1
            
            current = r - l + 1
            maxx = max(current, maxx)
            sett.add(s[r])
        return maxx

            
                





        