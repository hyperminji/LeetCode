class Solution:
    def isHappy(self, n: int) -> bool:
        #1.각 자릿수를 구하고 제곱해서 더한다
        #2. 1 번을 지속하다가 순환고리가 생기는지 확인 -> while
        #3. 순환고리가 생기면 false, 1나오면 true -> set
        
        cctv = set()
        n = str(n)
        
        while n != '1':
            cctv.add(n)
            number = 0
            for i in n:
                number = number + int(i)*int(i)
            n= str(number)
            
            if n in cctv:
                return False
        return True