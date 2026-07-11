class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Same as https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
        where hash set just has val. Maintain k to where we need to replace and keep i for
        traversing
        """
        k = 0

        for i in range(len(nums)):
            if nums[i] == val:
                continue
            nums[k] = nums[i]
            k += 1
        
        return k
        #TC: O(N), SC: O(1)