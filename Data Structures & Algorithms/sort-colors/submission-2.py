class Solution:
    def sortColors(self, nums: List[int]) -> None:
      count0 = nums.count(0)
      count1 = nums.count(1)
      count2 = nums.count(2)

      nums[:] = [0]*count0 + [1]*count1 + [2]*count2

            
                

        
#i am going to write my code
"""hello
what about u
comon"""

        
"""
        Do not return anything, modify nums in-place instead.
"""
        