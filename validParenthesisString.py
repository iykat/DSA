"""https://leetcode.com/problems/valid-parenthesis-string/"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        open_stack =[]
        star = [] 
        l = len(s)
        
        for i in range(l):
            if s[i] == '(':
                open_stack.append(i)
            elif s[i] == '*':
                star.append(i)
            else:
                if open_stack:
                    open_stack.pop()
                elif star:
                    star.pop()
                else:
                    return False
                
        # now process leftover opening brackets
        while open_stack:
            if not star:
                return False
            elif open_stack[-1] < star[-1]:
                open_stack.pop()
                star.pop()
            else:
                return False
        return True
        
        
        
