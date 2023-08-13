import numpy as np

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        coordinates= np.array(coordinates)
        if np.linalg.matrix_rank(coordinates[1:] - coordinates[0]) == 1:
            return True
        return False
        