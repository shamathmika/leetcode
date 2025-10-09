class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {} # This will store all the numbers and their indices in a map

        for index, num in enumerate(nums): # enumerate gives the index and list item in the array
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], index]
                
            num_to_index[num] = index
