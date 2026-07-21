class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        So basically, just increment the last element of the array by 1. But
        the issue is that the last digit can be 9. Maybe we can run a loop 
        from last element to first. If at any point we have a number other 
        than 9, increment and return. Else if it is 9, make it 0 and keep going
        back till 0. Now if all digits are 9, then we need to prepend with a [1]
        """
        i = len(digits) - 1
        while i >= 0:
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0
            i -= 1
        
        return digits if (digits[0] != 0) else ([1] + digits)
        # TC: O(N), SC: O(N)