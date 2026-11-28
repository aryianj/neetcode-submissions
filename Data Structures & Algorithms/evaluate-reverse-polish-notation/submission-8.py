class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        exp = []
        for t in tokens:
            if t.lstrip('-').isdigit():
                exp.append(int(t))
            else:
                a, b = exp.pop(), exp.pop()
                if t == '+':
                    exp.append(a + b)
                elif t == '-':
                    exp.append(b - a)
                elif t == '*':
                    exp.append(a * b)
                else:
                    exp.append(int(b / a))
        return int(exp[0])