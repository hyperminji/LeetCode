class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        firstcitycost = [i for i,j in costs]
        diff = [j-i for i,j in costs]
        
        total= sum(firstcitycost)
        #print(total)
        diff.sort()
        #print(diff)
        for i in range(len(costs)//2):
            total += diff[i]
        return total