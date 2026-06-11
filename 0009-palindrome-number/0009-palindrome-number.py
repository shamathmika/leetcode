class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Convert to string, start from left and right and return
        true if all numbers same till l == r. Or try the same
        with an array. With string, we can also do reverse and
        check if its the same.
        Let's say the number is 12321. Do mod 10, we get 1. Divide 
        the number by 10, we get 1232. Check if 1 == 1232. No, so
        get the mod again. We get 2. Multiply 1 by 10 and add 2.
        Now we check 12 == 123. Since 3 is just an additional number
        we also need to check 12 == 123//10. Which it is, so return 
        true. Else return false
        """
        # Brute Force - array and reverse
        if x < 0:
            return False
            
        n = list()
        while x > 0:
            n.append(x % 10)
            x = x // 10
        
        return n == n[::-1]
        # TC: O(n), SC: O(n)

        # # Brute Force - array and manual compare
        # if x < 0:
        #     return False

        # n = list()
        # while x > 0:
        #     n.append(x % 10)
        #     x = x // 10
        
        # l = len(n)
        # for i in range(l):
        #     if n[i] != n[l-i-1]:
        #         return False
        # return True
        # # TC: O(n), SC: O(n)

        # # Brute Force - string conversion and reverse
        # s = str(x)
        # return s == s[::-1]
        # # TC: O(n), SC: O(n)
        
        # # Brute Force - string conversion and manual compare
        # s = str(x)
        # l = len(s)
        # for i in range(l):
        #     if s[i] != s[l-i-1]:
        #         return False
        # return True
        # # TC: O(n), O(n)
