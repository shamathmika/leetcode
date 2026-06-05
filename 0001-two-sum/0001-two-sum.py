class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # One pass map solution
        # We have an empty map. When we come across a number, check
        # if target - that number is present in the map, if so,
        # return the indices. Else, add this number to the map
        l = len(nums)
        m = defaultdict(int)
        for i in range(0, l):
            diff = target - nums[i]
            if diff in m:
                return [m[diff], i]
            m[nums[i]] = i
        
        # # Two pass map solution
        # # In first pass, create a map 
        # # m = {
        # #   2: [0],
        # #   7: [1],
        # #   ...
        # # }
        # # In the second pass, go from right to left. Check if
        # # target - nums[i] is in m, and return the first index
        # # of the value present. This way, if nums was [3, 3],
        # # you will have m = {3: [0, 1]}, and when you start nums
        # # from right, you have index 1, and m[3] = [0, 1]. First
        # # value is 0
        # l = len(nums)
        # m = defaultdict(list)
        # for i in range(0, l):
        #     m[nums[i]].append(i)

        # for i in range(l-1, 0, -1):
        #     diff = target - nums[i]
        #     if diff in m and m[diff][0] != i: # second check because of this case: nums = [2, 4, 9, 3], target = 6. This returns [3, 3] without the second check
        #         return [m[diff][0], i]
        # # TC: O(n), SC: O(n)
        
        
        # # Brute Force
        # # For each element i starting from 0, check every other element 
        # # (start from i+1), if the sum of those two add up to the target
        # l = len(nums)
        # for i in range(0, l-1):
        #     for j in range(i+1, l):
        #         if (nums[i] + nums[j] == target):
        #             return [i, j]
        # # TC: O(n^2), SC: O(1)
