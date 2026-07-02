class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """
        So we have two nums lists - things that could happen:
        1. nums1 and nums2 have numbers mixed which would actually need to be
        sorted into nums1
        2. nums1 has all the smaller numbers and nums2 has all the bigger numbers
        or vice versa. But I think this is the same case as 1
        3. Only nums1 has values or vice versa
        4. Both are empty - Not possible as per conditions
        Brute force would be to just merge the two lists (copy the nums2 elements
        in place of 0 in nums1) and then sort with nums1.sort(). TC would be
        O(n + (n+m)log(n+m))
        What else we can do is, move all the elements in nums1 to the end of nums1
        so it becomes [1, 2, 3, 1, 2, 3]. Then start at nums1[n] (n is nums2's size)
        Compare and copy the elements to nums1 in its right position. Pass 1 we
        would have [1, 2, 3, 1, 2, 3]. Pass 2 we would have [1, 2, 3, 1, 2, 3].
        Pass 3 we would have [1, 2, 2, 1, 2, 3]. Pass 4 we would have [1, 2, 2, 
        3, 2, 3]. Pass 5 we would have [1, 2, 2, 3, 5, 6]. Time complexity would
        be O(n + m) which at max is 400
        """
        for i in range(m, 0, -1):
            nums1[n + i - 1] = nums1[i - 1] # Copy nums1 to the end of nums1
        
        n1 = n # The starting point of nums1 now
        n2 = 0
        i = 0 # Where we need to replace the numbers in nums1
        while n1 < (n + m) and n2 < n:
            if nums1[n1] <= nums2[n2]:
                nums1[i] = nums1[n1]
                n1 += 1
            else:
                nums1[i] = nums2[n2]
                n2 += 1
            
            i += 1
        
        while n1 < (n + m): # If any elements remain in nums1
            nums1[i] = nums1[n1]
            n1 += 1
            i += 1
        
        while n2 < n: # If any elements remain in nums2
            nums1[i] = nums2[n2]
            n2 += 1
            i += 1
        
        return
        # TC: O(n+m), SC: O(1)