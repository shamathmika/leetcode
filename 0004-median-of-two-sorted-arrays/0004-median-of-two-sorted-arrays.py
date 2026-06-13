class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Brute force we probably would iterate through both the array
        fully, copy them to another array and find the median from
        the new array. That would be O(tot) where tot is the number of
        elements in both arrays. What we can also do instead (with the 
        same TC) is instead of creating a new array, do merge sort on
        the fly. So, two pointers on the two arrays. Define a function
        which only returns the min value at that point. Run a loop and
        call this function until the number just before median is reached.
        This is so that if tot is even, we need two mins to be added and
        divide by 2. For a tot of 3, run the loop once so that 2nd smallest
        element can be returned. For tot = 4, run the loop once, so that
        second and third smallest elements can be returned. So for odd
        cases, run upto (l1 + l2) / 2. For even cases, run upto ((l1 + l2)
        / 2) - 1.
        """
        l1 = len(nums1)
        l2 = len(nums2)
        tot = l1 + l2
        p1, p2 = 0,0

        def getmin():
            nonlocal p1, p2 # refers to the global p1, p2
            if p1 < l1 and p2 < l2: # both arrays have values
                if nums1[p1] < nums2[p2]:
                    ans = nums1[p1]
                    p1 += 1
                else:
                    ans = nums2[p2]
                    p2 += 1
            elif p2 == l2:
                ans = nums1[p1]
                p1 += 1
            else:
                ans = nums2[p2]
                p2 += 1
            return ans # this will have the current min of both the arrays

        if tot % 2 != 0: # odd
            for _ in range(tot // 2):
                _ = getmin() # ignore the minimums until we reach median - 1 element
            return getmin() # get the next minimum, itll be the median
        else:
            for _ in range((tot // 2) - 1):
                _ = getmin() # ignore until median - 2 element
            return (getmin() + getmin()) / 2
        
        # TC: O(n), SC: O(1)