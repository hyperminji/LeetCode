class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for i in tokens:
            if i in operators:
                second, first = stack.pop(),  stack.pop()

                if i == '+':
                    temp = first+second
                elif i == '-':
                    temp = first - second
                elif i == '*':
                    temp = first * second
                else:
                    temp = int(first/second)
                
                stack.append(temp)

            else:
                stack.append(int(i))
        return stack[0]
                