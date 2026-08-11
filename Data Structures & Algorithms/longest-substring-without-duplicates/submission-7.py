class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        keys=set()
        l=0
        maxlength=0

        for r in range(len(s)):

            while s[r]  in keys:
                keys.remove(s[l])
                l +=1

            keys.add(s[r])
            maxlength=max(maxlength,r-l+1)

        return maxlength

        

                

            


        
       