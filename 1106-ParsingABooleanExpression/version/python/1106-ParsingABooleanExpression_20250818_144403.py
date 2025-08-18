# Last updated: 8/18/2025, 2:44:03 PM
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for ch in expression:
            if ch == ',':
                continue
            elif ch in ['t', 'f', '!', '&', '|', '(']:
                stack.append(ch)
            elif ch == ')':
                vals = []
                while stack[-1] != '(':
                    vals.append(stack.pop())
                stack.pop()  # remove '('
                op = stack.pop()  # operator
                if op == '!':
                    stack.append('t' if vals[0] == 'f' else 'f')
                elif op == '&':
                    stack.append('t' if all(v == 't' for v in vals) else 'f')
                elif op == '|':
                    stack.append('t' if any(v == 't' for v in vals) else 'f')

        return stack[-1] == 't'
        
