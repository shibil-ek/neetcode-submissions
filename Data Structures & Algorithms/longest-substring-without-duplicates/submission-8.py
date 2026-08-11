class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        keys=""
        l=0
        maxlength=0

        for r in range(len(s)):

            while s[r]  in keys:
                keys=keys[1:]
                l +=1

            keys += s[r]
            maxlength=max(maxlength,r-l+1)

        return maxlength

        

                

            


        
       