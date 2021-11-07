import collections

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter= collections.Counter(tasks)
        result = 0
        
        while True:
            count_sub = 0
                      
            
            for task, _ in counter.most_common(n + 1):
                count_sub = count_sub + 1
                result = result +1
                
                counter.subtract(task)
                
                counter = counter + collections.Counter()
                
                
            if not counter:
                break
                
            result = result + (n- count_sub +1)
        return result
        
