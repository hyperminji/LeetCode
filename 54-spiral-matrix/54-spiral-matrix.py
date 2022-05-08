class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #
        result = []
        count = 0
                
        while len(matrix) != 0 and len(matrix[0]) != 0:
            if count % 4 == 0:
                result += matrix.pop(0)
        
            if count % 4 == 1:
                for i in range(len(matrix)):
                    result.append(matrix[i].pop())
        
            if count % 4 == 2:
                result += matrix.pop()[::-1]
            
            if count % 4 ==3:
                for i in range(len(matrix))[::-1]:
                    result.append(matrix[i].pop(0))
                
            count += 1
        
        return result
            
    
        