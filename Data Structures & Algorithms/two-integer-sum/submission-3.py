class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        d={}

        for i in range(n):
            needed = target - nums[i]
            if needed in d:
                return [d[needed],i]
            else:
                d[nums[i]] = i

            #  for i in range(n):
            # needed = target - nums[i]
            # if needed in nums:
            #     return [i,index of needed]
            # else:
            #     d[nums[i]] = i


        