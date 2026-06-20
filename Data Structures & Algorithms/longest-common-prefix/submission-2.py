class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        shortest_word = ""
        shortest_word_len = float("inf")
        for i in range(len(strs)):
            if shortest_word_len > len(strs[i]):
                shortest_word_len = len(strs[i])
                shortest_word = strs[i]

        

        l = 0
        

        for i in strs:
            while l < len(shortest_word):
                if shortest_word[l] != i[l]:
                    shortest_word = shortest_word[:l]
                else:
                    l+=1
                    
            l = 0
            
        return shortest_word





        
                
        



       
        
            
            
       
        

            



        