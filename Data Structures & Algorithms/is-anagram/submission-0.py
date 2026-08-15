class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds={}
        dt={}
        for ch in s:
            if ch in ds:
                ds[ch] += 1
            else:
                ds[ch] = 1

        for ch in t:
            if ch in dt:
                dt[ch] += 1
            else:
                dt[ch] = 1
        
        if dt == ds:
            return True
        else:
            return False
        
            
       
       
        