class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        differ = arr[1]- arr[0]
        for i in range(1, len(arr)):
            if arr[i]-arr[i-1] != differ:
                return False
        return True
        
        