class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        With python, we can just use strip() to remove white spaces from
        the beginning and end of s. Then split it for " " and return the
        length of -1th element (last element).
        Without that, we could start from the end of the string, if it is
        whitespace, keep going left. The moment we reach any character other
        than space, start counting length. Return length when you reach
        space again.
        This requires two loops, instead, we can also do in one loop by
        again starting from the end. If we come across a space, check if
        the length we're counting is > 0. If so we have crossed the last word
        and return length. If not, it is a character, add to length count.
        Else it is trailing white space which can be ignored
        """
        # One loop
        l = 0
        i = len(s) - 1
        while i >= 0:
            if s[i] != " ":
                l += 1
            elif s[i] == " " and l > 0:
                return l
            
            i -= 1
        
        return l
        # TC: O(N), SC: O(1)

        # Python function
        # return len(s.strip().split(" ")[-1])
        # return len(s.split().pop()) # also works
        # TC: O(N), SC: O(1)