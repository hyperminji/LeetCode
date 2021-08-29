class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #($,@)  -> (@, $)
        second_matrix = copy.deepcopy(matrix)
        
        num = len(matrix[0])
        for left in range(num):
            for right in range(num-1, -1, -1):
                l_index = num - 1
                matrix[right][abs(left - l_index)] = second_matrix[left][right]
        