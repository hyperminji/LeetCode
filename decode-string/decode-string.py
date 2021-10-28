class Solution:
    def decodeString(self, s: str) -> str:
        # 스택 
        stack = [] 
        curNum = 0 
        answer = ''
        for c in s:
            if c == '[':
                stack.append(answer)
                stack.append(curNum)
                answer = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                preString = stack.pop()
                answer = preString + num*answer
            elif c.isdigit():     
                curNum = curNum*10 + int(c)
            else:
                answer = answer + c
        return answer       