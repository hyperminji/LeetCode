class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0]
        
        for i in range(1, n+1):
            result.append(result[i & (i -1)]+ 1)
        return result
    
    #count = 0
    #while x !=0:
    #   count = count + 1
    #   x = x & (x-1)
    #return count 