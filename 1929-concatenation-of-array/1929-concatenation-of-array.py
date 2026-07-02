class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """
        Multiple ways to do this in python. Listing down all the ways I can think of here
        1. Just return nums + nums. Time complexity and space complexity for this is O(2n)
        because + on a list takes O(n+m) and it allocates a new memory of the space n + m
        2. Just create a new list ans and in two separate loops (looping through nums),
        append ans with the numbers from nums. TC is O(2n) and SC is O(2n)
        3. Create ans = [0] * (2 * n) - this creates the list of size 2n initialized to 0. 
        We need to create with the size and initialize since we can't "append" in one loop 
        otherwise. TC is O(n) since its just one loop and we update i and i+n in one go. SC
        is O(2n)
        4. Python has a method called extend which extends a list in place. So you just do
        nums.extend(nums) and then return it. This also has TC of O(n) and SC O(n) since it
        just appends n elements to existing memory
        """
        nums.extend(nums)
        return nums
    
    # TC: O(N), SC:O(N)