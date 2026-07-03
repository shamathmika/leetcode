class Solution:
    def isValid(self, s: str) -> bool:
        """
        This one should be easy. We maintain a map of close to open to match different brackets.
        Eg, one entry would be ']': '[]' and so on. Then iterate through s and push any open 
        bracket to a stack (just an array). If we encounter a close bracket, check if its in the
        map and then pop the last element from the array and match it. If the stack is empty at
        the end, return true, else false
        """
        closetoopen = {
            ']' : '[',
            ')' : '(',
            '}' : '{'
        }

        stack = []
        for c in s:
            if c in closetoopen:
                if len(stack) == 0:
                    return False
                o = stack.pop()
                if o != closetoopen[c]:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0
        # TC: O(s), SC: O(s)
