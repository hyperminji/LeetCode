class Solution:
    def numSquares(self, n: int) -> int:
        if n < 2:
            return n
        
        sqr_list = []
        i = 1
        while i * i <= n:
            sqr_list.append(i * i)
            i += 1
            
        check_list = {n}
        
        count = 0
        while len(check_list) > 0:
            count = count + 1
            tmp = set()
            for item in check_list:
                for square in sqr_list:
                    if item == square: 
                        return count
                    if item < square:
                        break
                    tmp.add(item - square)
                    
            check_list = tmp
            
        return count
        