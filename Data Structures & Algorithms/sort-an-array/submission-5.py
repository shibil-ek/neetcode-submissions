class Solution:
    def sortArray(self, arr: List[int]) -> List[int]:

        if len(arr) <= 1:
            return arr

        mid = len(arr)//2

        left=arr[:mid]
        right=arr[mid:]

        left_sorted = self.sortArray(left)
        right_sorted = self.sortArray(right)

        return self.merge(left_sorted,right_sorted)

    def merge(self,left,right):
        result=[]
        i=0
        j=0

        while len(left) > i and len(right) > j:
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

        