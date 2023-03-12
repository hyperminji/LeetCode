class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boat = 0
        people= sorted(people)
        light = 0
        N = len(people)
        
        for n in range(N-1, -1, -1):
            if light > n: break
            elif light == n:
                boat += 1
                break
            if people[n] + people[light] <= limit:
                light += 1
            boat+= 1
        return boat
   
        
        