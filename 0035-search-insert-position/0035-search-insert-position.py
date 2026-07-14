class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        O(log n) TC and sorted array, so it has to be a binary search.
        At each mid point, check if the target is equal to mid, if so
        return. Else, check if target is lesser or greater than mid. If
        greater, check if the next element is greater than target. If so
        return next element's index. If lesser, check if prev element is
        lesser than target and return the current element
        """
        if target < nums[0]:
            return 0
        if target > nums[len(nums)-1]:
            return len(nums)
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
                if (m - 1) >=0 and target > nums[m - 1]:
                    return m
            elif nums[m] < target:
                l = m + 1
                if target < nums[m + 1]:
                    return (m + 1)
        
        # TC: O(log n), SC: O(1)