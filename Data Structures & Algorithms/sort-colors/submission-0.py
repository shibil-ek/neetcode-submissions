class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] >= nums[j]:
                    nums[i],nums[j] = nums[j],nums[i]

        
#i am going to write my code
"""hello
what about u
comon"""

        
"""
        Do not return anything, modify nums in-place instead.
"""
        