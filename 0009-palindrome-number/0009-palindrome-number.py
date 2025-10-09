class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        xcopy = x
        reverse = 0

        if x < 0:
            return False

        while x != 0:
            reverse = reverse * 10 + (x%10)
            x = x//10
        
        return xcopy == reverse