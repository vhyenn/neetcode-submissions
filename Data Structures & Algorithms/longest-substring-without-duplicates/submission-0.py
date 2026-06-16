class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxx = 0
        
        for i in range(len(s)):
            myset = set()
            current_len = 0
            for j in range(i, len(s)):
                if s[j] in myset:
                    maxx = max(current_len, maxx)
                    current_len = 0
                    myset = set()
                    myset.add(s[j])

                else:
                    current_len += 1
                    myset.add(s[j])
                    maxx = max(maxx, current_len)
                
            
            
                
        
        return maxx


        