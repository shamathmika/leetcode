class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        """
        This is a very simple question. Basically go over every
        element and check the sum of the digits and compare with
        i. I did the following implementation but got to know I 
        can improve this in 2 different ways. 
        1. instead of manually calculating the sum of the digits
        which does it in python, use built in functions which runs
        in CPython (so C and is faster) like map and sum
        if sum(map(int, str(nums[i]))) == i - return i
        that^ basically takes nums[i] (eg 123) and converts it to
        str ("123") and then converts each char to int (here int is
        a function that runs on top of the str's output - [1, 2, 3])
        sum then calculates 1 + 2 + 3.
        2. Since 1000 is the max that nums[i] can be, 999 is the one
        with a max sum (9 + 9 + 9 = 27). So we only need to go upto
        27th index. Can ignore things after that.
        """
        for i in range(len(nums)):
            s = 0
            while nums[i] != 0:
                s += nums[i] % 10
                nums[i] = nums[i] // 10
            
            if s == i:
                return i
        return -1