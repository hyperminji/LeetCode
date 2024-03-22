class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0

        for i in range(1, len(height) - 1):
            column = min(max(height[:i]), max(height[i:])) - height[i]
            if column > 0:
                result = column +result

        return result