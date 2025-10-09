class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        '''
        a: 1 (2) 7 
        b: (1) 4 6 8
        [1 1 2] [4 6 7 8]

        a: 1 2 (3) 4
        b: 1 1 (2) 4 5 8 9 11
        [1 1 1 2 2 3] [4 4 5 8 9 11]

        We are essentially doing binary search on one of the arrays - particularly the smaller one (by length)
        For simplicity, we set a and b as nums1 and nums2 and keep a as the smaller array
        We need to find the left half and right half of the "imaginary merged list"
        So what we do is find the first half. The answer will be the at the edge of the first half
        '''
        a, b = nums1, nums2
        total = (len(a) + len(b))
        half =  total // 2

        if len(a) > len(b):
            b, a = a, b
        
        l, r = 0, len(a) - 1 # Traverses the smaller array

        while True:
            i = (l + r) // 2 # Find mid point of a
            j = half - i - 2 # whatever is remaining from the "half", pick that from b

            # We only are worried about the boundaries of the left and right parts of a and b
            aleft = a[i] if i >= 0 else float('-inf') # aleft is the rightmost element of the left part
            aright = a[i+1] if i+1 < len(a) else float('inf') # aright is the leftmost element of the right part
            bleft = b[j] if j >= 0 else float('-inf')
            bright = b[j+1] if j+1 < len(b) else float('inf')

            if aleft <= bright and bleft <= aright: # this means we found our first half of the "imaginary merged array"
                # yayyy median
                if total % 2 != 0:
                    return min(aright, bright) # For odd, its the min of the right part of a or b
                else:
                    return float((max(aleft, bleft) + min(aright, bright))) / 2 # If even, choose the max of the first half of the merged array and the min of the right part of the merged array
            
            if aleft > bright: # This means, we need to use more of b than a
                r = i - 1
            else: # This means we need to use more of a than b
                l = i + 1

# TC: O(log(min(m, n))
# SC: O(1)