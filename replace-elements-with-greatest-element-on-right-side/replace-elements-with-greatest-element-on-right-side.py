class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        member = -1
        i = len(arr) -1 
        while i >= 0:
            temp = arr[i]
            arr[i] = member
            if temp > member:
                member = temp
            i = i-1
        return arr
        