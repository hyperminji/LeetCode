class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        count = collections.defaultdict(int)
        for line in wall:
            linesum = 0
            for brick in line[:-1]:
                linesum+= brick
                count[linesum]+=1
        if not len(count):
            return len(wall)
        return len(wall)-max(count.values())
        